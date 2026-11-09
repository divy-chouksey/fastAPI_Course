from fastapi import APIRouter, UploadFile, File, Form , HTTPException
from google.genai._gaos.types.interactions.annotation import FileCitationParam
from services.image import *
from services.vision import *
import uuid

router = APIRouter(prefix="/analyse",tags = ["analyse"])



async def process_single_image(file:UploadFile):

    content = await file.read()

    validation = validate_image(content , file.content_type)

    if not validation["is_valid"]:
        raise HTTPException(status_code=400 ,detail = validation["message"])

    processed = resize_if_needed(content)

    ext = file.filename.split(".")[-1] if "." in file.filename else "jpg"
    unique_name = f"{uuid.uuid4().hex}.{ext}"

    save_image(processed , "uploads" , unique_name)

    analysis = await analyze_image(processed , file.content_type)

    print(f"Analysis result for {file.filename}: {analysis}")

    return analysis

@router.post("/")
async def analyse_image(file: UploadFile = File(...)):
    """
    Endpoint to analyse a single image for disease detection.
"""
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image.")   

    result = await process_single_image(file)
    return {
        "filename":file.filename,
        "content_type":file.content_type,
        "analysis":result,
        "message":"Analysis completed successfully",
    }

@router.post("/batch")
async def analyse_batch(files: list[UploadFile] = File(...)):
    """
    Endpoint to analyse a batch of images for disease detection.
"""
    results = []
    for file in files:
        if not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image.")
        result = await process_single_image(file)
        results.append(result)
    return results