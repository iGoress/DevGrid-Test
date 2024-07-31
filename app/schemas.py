from pydantic import BaseModel
from app.models import WeatherData

class WeatherResponse(BaseModel):
    user_id: str
    timestamp: str
    data: WeatherData