import httpx
from app.config import OPENWEATHER_API_KEY, OPENWEATHER_API_URL

async def fetch_weather_data(city_id: int):
    async with httpx.AsyncClient() as client:
        params = {
            "id": city_id,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }
        response = await client.get(OPENWEATHER_API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return {
            "city_id": data["id"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"]
        }