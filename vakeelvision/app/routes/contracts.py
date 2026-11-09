from fastapi import APIRouter , UploadFile, File, HTTPException
import os
from config import ALLOWED_EXTENSIONS, MAX_FILE_SIZE_MB , UPLOADS_DIR
import uuid
from services.document_parser import extract_text
from models import Contract
from database import contracts_collection
from bson import ObjectId

router = APIRouter(
    prefix="/contracts",
    tags=["contracts"],
)

@router.post("/upload")
async def upload_contract(
    file: UploadFile = File(...)
):
    """
    Upload a PDF or TXT contract for analysis.
"""
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF and TXT files are allowed.")

    content = await file.read()

    size_mb = len(content) / (1024 * 1024)  # Convert bytes to megabytes
    if size_mb > MAX_FILE_SIZE_MB:
        raise HTTPException(status_code=400, detail=f"File size exceeds the maximum limit of {MAX_FILE_SIZE_MB} MB.")

    os.makedirs(UPLOADS_DIR, exist_ok=True)
    unique_name = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(UPLOADS_DIR, unique_name)
    # Implement the logic to handle contract upload
    with open(file_path, "wb") as f:
        f.write(content)
    
    parsed = extract_text(file_path)

    contract_data = Contract(
        filename=unique_name,
        original_name=file.filename,
        text_content=parsed["text"] if isinstance(parsed,dict) else parsed,
        page_count=parsed.get("page_count", 0),
        word_count=parsed.get("word_count", 0)
    )

    doc = contract_data.model_dump()
    result = contracts_collection.insert_one(doc)
    contract_data.id = str(result.inserted_id)

    return {
        "message" : "File uploaded and processed successfully",
        "contract":contract_data.model_dump(),
        "id": contract_data.id
    }

@router.get("/")
async def list_contracts():
    contracts = []
    for doc in contracts_collection.find({},{"text_content":0}):
        contract = Contract(**doc)
        contract.id = str(doc["_id"])
        contracts.append(contract.model_dump())

    return {"contracts" : contracts}

@router.get("/{contract_id}")
async def get_contract(contract_id:str):
    doc = contracts_collection.find_one({"_id":ObjectId(contract_id)})
    if not doc:
        raise HTTPException(status_code=404, detail="Contract not found")
    contract = Contract(**doc)
    contract.id = str(doc["_id"])
    return {"contracts" : contract.model_dump()}



