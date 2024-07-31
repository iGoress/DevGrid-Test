from fastapi.testclient import TestClient
from app.main import app

MOCK_RESPONSE_DATA = {
    "id": 123456,
    "main": {
        "temp": 20.0,
        "humidity": 80
    }
}

client = TestClient(app)

def test_collect_weather_data_return_ok():
    #TODO: Create mock to return value from fetch_weather_data
    response = client.post("/weather/", json={"user_id": "test_user"})
    assert response.status_code == 200
    assert response.json() == {"message": "Data collection complete"}

def test_get_progress_return_ok():
    response = client.get("/weather/progress",params={"user_id":"test_user"})
    assert response.status_code == 200
    progress = response.json().get("progress", 0)
    assert 0 <= progress <= 100

def test_get_progress_return_error():
    response = client.get("/weather/progress",params={"user_id":"not_found"})
    assert response.status_code == 404

def test_get_index_page_return_ok():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "DevGrid Test API"