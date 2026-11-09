from os import getenv
from qdrant_client.http import model
from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader  
from langchain_text_splitters import RecursiveCharacterTextSplitter  
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
import time

load_dotenv()
pdf_path = Path(__file__).parent / "data" / "sample.pdf"

#Pdf loader
loader = PyPDFLoader(str(pdf_path))

docs = loader.load()

#Text Splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

chunks = text_splitter.split_documents(documents = docs)

#Embedding the chunks using open Ai embeddings
# Embedding the chunks using Gemini embeddings
embeddings_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-2",
    google_api_key=getenv("GEMINI_API_KEY")  # if your .env uses GEMINI_API_KEY
)

batch_size =  40
vector_store = None


for i in  range(0, len(chunks), batch_size):
    batch = chunks[i: i+ batch_size]
    print(f"Uploading batch {i//batch_size + 1}/{(len(chunks) + batch_size -1 ) // batch_size} ...")

    if vector_store is None:
        vector_store = QdrantVectorStore.from_documents(
            documents=batch,
            embedding=embeddings_model,
            collection_name="new_collection_2",
            url="http://localhost:6333"   # <--- http:// instead of https://
        )
    else:
        vector_store.add_documents(batch)

    time.sleep(30)


print("Vector store created and documents stored successfully!")

 






