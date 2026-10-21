from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables
from routes.reviews import router as reviews_router


#with this i can control what happens when fastapi 
# is started and what happens when it is shutdown
@asynccontextmanager
async def lifespan(app:FastAPI):
    create_tables()
    print("Database tables created")
    yield
    #shutdown : cleanup here
    print("Shutting Down the app")

app = FastAPI(
    title="Rangmanch",
    description="Theatre reviews API for Pune Rangmanch",
    lifespan=lifespan
)

app.include_router(reviews_router)

@app.get("/")
def root():
    return {"message" : "Welcome to rangmanch review API"}
