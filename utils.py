import os
import httpx
from cache.async_lru import AsyncLRU
from logger_config import logger
from dotenv import load_dotenv

load_dotenv()


@AsyncLRU(maxsize=128)
async def ip_to_loc(ip):
    response = httpx.get(f"https://ipinfo.io/{ip}?token={os.environ.get('IPINFO_TOKEN')}")
    if response.status_code != 200:
        logger.error(f"ip response: {response.text}, ")
    loc = response.json().get('loc')
    lat, lon = loc.split(',')
    return lat, lon


async def openweather(lat, lon):
    weather_response = httpx.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric"
                                 f"&appid={os.environ.get('API_WEATHER_KEY')}",
                                 )
    if weather_response.status_code != 200:
        logger.error(f"weather_response: {weather_response.text}")
    return weather_response.json()


async def makeresponse(weather_response):
    responseJSON = {"city": weather_response['name'],
                    "temp": weather_response['main']['temp'],
                    "conditions": weather_response['weather'][0]['description'],
                    "wind": weather_response['wind']
                    }
    return responseJSON
