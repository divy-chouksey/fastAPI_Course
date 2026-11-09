from fastapi import APIRouter, HTTPException
from models import TravelRequest
from fastapi.responses import StreamingResponse
import json
from services.weather import fetch_weather
from services.places import fetch_places
from services.currency import fetch_currency_rates
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix='/stream', tags=['Stream'])


def format_sse(data:str , event : str = None)-> str:
    json_data = json.dumps(jsonable_encoder(data))
    return f"data : {json_data}\n\n" if event is None else f"event: {event}\ndata: {json_data}\n\n"


@router.post("/plan", response_class=StreamingResponse)
async def stream_generator(request : TravelRequest):
    yield format_sse({"message":"Starting travel plan stream..."},event="start")
    yield format_sse({"message":"Fetching weather data..."},event="weather")
    weather_data = await fetch_weather(
            destination=request.destination,
            start_date=request.start_date,
            end_date=request.end_date
    )
    yield format_sse({"message":"Weather data fetched successfully","data":weather_data},event="weather")
    yield format_sse({"message":"Fetching travel options..."},event="options")
    places_data = await fetch_places(request.destination)
    yield format_sse({"message":"Travel options fetched successfully","data":places_data},event="options_complete")
    yield format_sse({"message":"Fetching currency rates..."},event="currency")
    currency_rates = await fetch_currency_rates(request.base_currency)
    yield format_sse({"message":"Currency rates fetched successfully","data":currency_rates},event="currency_complete")





async def stream_travel_plan(request:TravelRequest):
    """Stream the travel plan updates (Server Sent Events)"""
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


    return StreamingResponse(
          stream_generator(request),
          meadia_type="text/event-stream",
          headers={"Cache-Control": "no-cache" , "Connection": "keep-alive"}

    )


    