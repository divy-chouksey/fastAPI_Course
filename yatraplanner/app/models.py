from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class TravelRequest(BaseModel):
    destination: str
    start_date:date
    end_date:date
    base_currency: str="INR"


class WeatherResponse(BaseModel):
    date:str
    condition:str
    temperature_high:float
    temperature_low:float
    humidity:float
    rain_chance:float


class PlaceModel(BaseModel):
    name:str
    description:str
    category:str
    rating:float
    estimated_time_hours:float
    entry_fee:Optional[float] = None


