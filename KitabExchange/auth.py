import os

from dotenv import load_dotenv
from fastapi import Header, HTTPException

load_dotenv()

API_KEY = os.getenv("KITABEXCHANGE_API_KEY")


def verify_api_key(x_api_key: str = Header()):
    if not API_KEY:
        raise HTTPException(status_code=503, detail="API key is not configured")
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key
