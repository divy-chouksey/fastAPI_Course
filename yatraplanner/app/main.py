from fastapi import FastAPI
from routes.planner import router as planner_router
from routes.stream import router as stream_router

app = FastAPI(
    title="YatraPlanner API",
    description="Aggregate travel data from multiple sources and provide a single plan with server sent events for real time updates",
)


@app.get("/")
async def get_root():
    return {
        "app":"Yatra Planner API",
        "version":"1.0.0",
        "endpoints":
        {
            "POST /plan":"Create a travel plan (Aggregated)",
            "GET /plan/stream":"Stream the travel plan updates (Server Sent Events)",
            "GET /plan/cache-stats":"View Cache statistics for the travel plan",
            "DELETE /plan/cache":"Clear the travel plan cache"
        }
    }

app.include_router(planner_router)
app.include_router(stream_router)