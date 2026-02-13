# Created by: Ahmad Tomeh
"""
API module for fetching weather data from the OpenWeatherMap API and handling potential errors.
- Uses the `requests` library to make HTTP requests to the API.
- Extracts and formats relevant weather data for use in the UI and charts.
"""

import requests
from config import API_KEY
from config import DATABASE_URL
import ui

# The API endpoint
url = DATABASE_URL

def get_weather(city):
    """Fetches weather data for a specified city from the OpenWeatherMap API."""

    params = {
    'q': city,
    'appid': API_KEY,
    'units': 'metric'
}
    # Make the API request and handle potential errors
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.RequestException:
        ui.api_error()
        return None

    # Extract and clean the relevant data
    clean = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp": round(data["main"]["temp"], 1),
        "feels_like": round(data["main"]["feels_like"], 1),
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"],
        "description": data["weather"][0]["description"]
    }

    return clean