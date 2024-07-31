# DevGrid-Test
Python Tech Test

## Requirements

- Python 3.10+
- Docker

## Installation

1. **Install dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Set Open Weather API Key**

   ```bash
   export OPENWEATHER_API_KEY="your_api_key_here"
   ```

## Running the Application

1. **Run Locally**

   Start the FastAPI application locally with:

```bash
   uvicorn app.main:app --reload --port 8080
```

   The application will be available at `http://127.0.0.1:8080`.

2. **Run with Docker**

   Build and run the Docker container:

   ```bash
   docker build -t weather_service .
   docker run -p 8080 -e OPENWEATHER_API_KEY=a3c05c5c3c85264e47c2050466f23be0 weather_service
   ```

## Testing

  To run the tests, use:

  ```bash
  pytest --cov=app
  ```

  You can also test manually using Postman, the collection is vailable in project  
  ```bash
  DevGrid-Test.postman_collection.json
  ```