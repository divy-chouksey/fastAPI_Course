from fastapi import FastAPI
from database import create_tables,get_session
from routes.user import router as user_router
from routes.book import router as book_router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Creating database tables.......")
    create_tables()
    yield
    print("app is shutting down")



app = FastAPI(
    title="KitabExchange API",
    version="1.0.0",
    description="API for buying and selling books",
    lifespan=lifespan
)

app.include_router(user_router)
app.include_router(book_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to KitabExchange API"}


