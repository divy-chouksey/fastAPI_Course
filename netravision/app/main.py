from fastapi import FastAPI
from router import analyse

app = FastAPI()


@app.get("/")
def get_root():
    return{
        "app":"NetraVision API",
        "version":"1.0.0",
        "endpoints":{
            "POST /analyse":"Upload an image for disease detection",
            "POST /analyse/batch":"Upload multiple images for disease detection",
            "GET /analyses":"Retrieve a list of all analyses perfomed",
            "GET /analyses/{analyses_id}":"Retrieve the results of a specific analysis by its ID"
        }
    }

app.include_router(analyse.router)
