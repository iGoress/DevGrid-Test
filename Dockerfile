FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV OPENWEATHER_API_KEY=a3c05c5c3c85264e47c2050466f23be0

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]