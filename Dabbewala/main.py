from contextlib import asynccontextmanager
from fastapi import FastAPI 
from database import create_tabels
from routes.orders import router as order_router
from routes.stats import router as stats_router


@asynccontextmanager
async def lifespan(app:FastAPI):
    create_tabels()
    print("Database tables created")
    yield
    print("Application Shutting down")


app = FastAPI(
    title="Dabbawala API",
    description="API for managing orders",
    version="1.0.0",
    lifespan=lifespan
    )

app.include_router(order_router)
app.include_router(stats_router)



@app.get("/health",tags=["health"])
def health_check():
    return {"status":"ok"}





    