import asyncio
from datetime import datetime
from fastapi import FastAPI, HTTPException

from app.models import WeatherRequest
from app.utils import fetch_weather_data
from app.cities import CITY_IDS

app = FastAPI()

weather_store = {}
progress_store = {}


@app.get("/")
async def get_progress():
    return "DevGrid Test API"


@app.post("/weather/")
async def collect_weather_data(request: WeatherRequest):
    print("chegou")
    user_id = request.user_id
    if user_id in weather_store:
        raise HTTPException(status_code=400, detail="User ID already exists")

    weather_store[user_id] = []
    progress_store[user_id] = 0
    counter_limit = 0
    for city_id in CITY_IDS:
        data = await fetch_weather_data(int(city_id))
        weather_store[user_id].append(
            {"timestamp": datetime.now().isoformat(), "data": data}
        )
        progress_store[user_id] += 1
        counter_limit += 1
        if counter_limit == 60:
            await asyncio.sleep(1)

    return {"message": "Data collection complete"}


@app.get("/weather/progress")
async def get_progress(user_id: str):
    if user_id not in progress_store:
        raise HTTPException(status_code=404, detail="User ID not found")

    total_cities = len(CITY_IDS)
    completed = progress_store[user_id]
    progress_percentage = int((completed / total_cities) * 100)

    return {"user_id": user_id, "progress": progress_percentage}
