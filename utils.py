import os
import httpx
from main import logger
from dotenv import load_dotenv

load_dotenv()

async def ip_to_loc(ip):
    response = httpx.get(f"https://ipinfo.io/{ip}?token={os.environ.get('IPINFO_TOKEN')}").json()
    logger.info(response)
    loc = response.get('loc')
    lat, lon = loc.split(',')
    return lat, lon

async def openweather(lat, lon):
    weather_response = httpx.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={os.environ.get('API_WEATHER_KEY')}")
    logger.info(weather_response)
    return weather_response.json()