import requests
import os
from fastapi import HTTPException
import requests

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = os.getenv("BASE_URL")



API_KEY = "fc991c99234d4526aae42339240310"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

async def fetch_weather_data(city: str):

    url = "https://api.weatherapi.com/v1/current.json"

    
    headers = {
    'accept': 'application/json'
    }
    params = {
        "key":API_KEY,
        "lang":"en",
        "q":city
    }
    try:
        
        response = requests.request("GET", url, headers=headers, params = params)
        data = response.json()
        weather = {
                "temperature": data["current"]["temp_c"],
                "humidity": data["current"]["humidity"],
                "description": data["current"]["condition"]["text"]
            }
        return weather
    except requests.exceptions.RequestException as e:
        
        print(f"Request failed: {e}")
        raise HTTPException(status_code=500, detail="Weather API request failed")
    except KeyError as e:
        
        # missing keys
        print(f"KeyError: Missing expected data in the response - {e}")
        raise HTTPException(status_code=500, detail="Missing data in Weather API response")
    
    except Exception as e:
        
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

