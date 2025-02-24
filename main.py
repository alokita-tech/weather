from fastapi import FastAPI
from services.weather_service import get_weather_data

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Weather API. Use /weather/{city} to get weather details"}

@app.get("/weather/{city}")
def weather(city: str):
    return get_weather_data(city)
