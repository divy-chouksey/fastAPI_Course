from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import init_db
from routes.contracts import router as contracts_router 
from routes.analysis import router as analysis_router


app = FastAPI(
    title="Vakeel Vision API",
    description="An API for Vakeel Vision, a platform that provides legal assistance and services through AI-powered solutions.",
    
)

@app.on_event("startup")
async def startup_event():
    init_db()  # Initialize the database and create collections if they don't exist




@app.get("/")
async def read_root():
    return {"app": "Vakeel Vision API",
            "endpoints":{
                "POST / contracts/upload":"Upload a PDF or TXT contract for analysis",
                "GET / contracts/":"Retrieve a list of all uploaded contracts",
                "GET / contracts/{contract_id}":"Retrieve a specific contract by ID",
                "POST / analysis/analyze/{contract_id}":"analyze a contract using AI and return insights",
                "GET / analysis/{analysis_id}":"Retrieve the results of a specific analysis by ID",
                "GET / analysis/contract/{contract_id}":"Retrieve all analyses for a specific contract by ID"
}}

app.include_router(contracts_router)
app.include_router(analysis_router)



