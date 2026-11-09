from fastapi import FastAPI
from app.routes.query import router as query_router


app = FastAPI(
    title="RAG API",
    description="This is a RAG API for querying PDF documents",
    version="0.1.0"
)

app.include_router(query_router)
