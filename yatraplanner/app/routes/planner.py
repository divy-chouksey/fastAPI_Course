from fastapi import APIRouter , HTTPException
from models import TravelRequest
from services.weather import fetch_weather
from services.places import fetch_places
from services.currency import fetch_currency_rates
import asyncio






router = APIRouter(prefix='/plan',tags=['Travel Plan'])
@router.post("/")
async def create_travel_plan(
    request:TravelRequest
):
    """Aggregate weather ,currency and places data into a single travel plan """
    if request.start_date > request.end_date:
        raise HTTPException(
            status_code=400,
            detail="Start date cannot be after end date"
        )


    trip_days = (request.end_date - request.start_date).days

    if trip_days < 1:
        raise HTTPException(
            status_code=400,
            detail="Trip duration must be at least 1 day"   
        )

    if trip_days > 14:
        raise HTTPException(
            status_code=400,
            detail="Trip duration cannot exceed 14 days"   
        )

    #Weather data , currency rate , and places data would be fetched and aggrefated here from multiple sources and returned as a single travel plan
    weather_data , places_data , currency_rates = await asyncio.gather(
        fetch_weather(
            destination=request.destination,
            start_date=request.start_date,
            end_date=request.end_date   
        ),
        fetch_places(request.destination),
        fetch_currency_rates(request.base_currency)
    )

    
    return{
        "message":"Travel plan created successfully",
        "weather_data":weather_data,
        "places_data":places_data,
        "currency_rates":currency_rates
    }