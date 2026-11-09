
from google.genai.types import GenerateContentConfig
from os import getenv
from google import genai
from dotenv import load_dotenv
from pathlib import Path
from fastapi import APIRouter
from langchain_qdrant import QdrantVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings




router = APIRouter(prefix="/query", tags=["query"])


env_path = Path(__file__).resolve().parent.parent.parent/ ".env"
load_dotenv(dotenv_path=env_path)

client = genai.Client(api_key=getenv("GEMINI_API_KEY"))



embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-2",
    api_key=getenv("GEMINI_API_KEY")
)

vector_db = QdrantVectorStore.from_existing_collection(
    collection_name="new_collection_2",
    embedding=embedding_model,
    url="http://localhost:6333"
)


@router.post("/")
async def query(question : str):
    results = vector_db.similarity_search(query=question)

    context = "\n\n---\n\n".join(
        f"[Page {result.metadata.get('page', 'unknown')}] {result.page_content}"
        for result in results
    )

    response = client.models.generate_content(
        model="models/gemini-3.5-flash",  # or gemini-2.0-flash / gemini-1.5-flash
        contents=f"Context:\n{context}\n\nQuestion: {question}",
        config=GenerateContentConfig(
            system_instruction="""You are a helpful assistant. Answer the user's question accurately 
            using only the provided context. If the answer is not in the context, state that clearly."""
        )
    )

    return {"response" : response.text}

    
    


