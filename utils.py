import os
import httpx
from logger_config import logger
from dotenv import load_dotenv

load_dotenv()

async def ip_to_loc(ip):
    response = httpx.get(f"https://ipinfo.io/{ip}?token={os.environ.get('IPINFO_TOKEN')}", trust_env=True)
    response.encoding = 'utf-8'
    logger.info("ip response: ",response.text)
    loc = response.json().get('loc')
    lat, lon = loc.split(',')
    logger.exception("Error in ip_to_loc func")
    return lat, lon

async def openweather(lat, lon):
    weather_response = httpx.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric"
                                 f"&lang=ru&appid={os.environ.get('API_WEATHER_KEY')}",
                                 trust_env=True
                                 )
    weather_response.encoding = "utf-8"
    logger.info('weather_response: ', weather_response.text)
    logger.exception("Error in openweather func")
    return weather_response.json()

async def makeresponse(weather_response):
    responseJSON = {"city": weather_response['name'],
                "temp": weather_response['main']['temp'],
                "conditions": weather_response['weather'][0]['description']
                }
    logger.info(responseJSON)
    logger.exception("Error in makeresponse func")
    return responseJSON