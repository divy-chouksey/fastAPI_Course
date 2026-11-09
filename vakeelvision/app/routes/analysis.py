from fastapi import APIRouter, HTTPException
from config import GEMINI_API_KEY
from database import contracts_collection , analysis_collection
from bson import ObjectId
from services.gemini_analyze import analyze_contract_gemini
from models import AnalysisResult
router = APIRouter(prefix="/analysis" , tags=["analysis"])

@router.post("/analyze/{contract_id}")
async def analyze_contract(contract_id:str):
    if not GEMINI_API_KEY:
        raise HTTPException(
            status_code=503,
            detail="Gemini API Key is not configured"
        )
    contract = contracts_collection.find_one({"_id":ObjectId(contract_id)})
    if not contract :
        raise HTTPException(
            status_code=404,
            detail="Contract not found"
        )
    if not contract.get("text_content"):
        raise HTTPException(
            status_code=400,
            detail="Contract has no text content"
        )
    contracts_collection.update_one({"_id":ObjectId(contract_id)},
    {"$set" : {"analysis.status" : "in_progress"}})
    result = await analyze_contract_gemini(contract["text_content"])
    doc = result.model_dump()
    insert_result = analysis_collection.insert_one(doc)
    result.id = str(insert_result.inserted_id)

    contracts_collection.update_one({"_id":ObjectId(contract_id)},
    {"$set" : {"analysis.status" : "completed","analysis.id":str(insert_result.inserted_id)}})

    return{
        "message":"Contract analyzed successfully",
        "analysis_id":result.model_dump(),
        "id":result.id
    }

@router.get("/{analysis_id}")
def get_analysis_by_id(analysis_id:str):
    doc = analysis_collection.find_one({"_id":ObjectId(analysis_id)})
    if not doc:
        raise HTTPException(status_code=404,detail="Analysis not found")
    
    result = AnalysisResult(**doc)
    result.id = str(doc["_id"])
    return {"analysis":result.model_dump()}

@router.get("/")
def get_all_analysis():
    analysis_results = []
    for doc in analysis_collection.find():
        result = AnalysisResult(**doc)
        result.id = str(doc["_id"])
        analysis_results.append(result.model_dump())
    return {"analysis_results":analysis_results}

@router.get("/contract/{contract_id}")
def get_analysis_by_contract_id(contract_id:str):
    analyses = []
    cursor = analysis_collection.find({"_id":ObjectId(contract_id)})
    for doc in cursor:
        doc["id"] = str(doc.pop("_id"))
        analyses.append(doc)
    return{"analyses":analyses,
    "total":len(analyses)}