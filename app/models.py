from pydantic import BaseModel

class WeatherData(BaseModel):
    city_id: int
    temperature: float
    humidity: int

class WeatherRequest(BaseModel):
    user_id: str