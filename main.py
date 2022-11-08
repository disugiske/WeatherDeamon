from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from logger_config import logger
from utils import ip_to_loc, openweather, makeresponse

app = FastAPI()


@app.get("/", response_class=JSONResponse)
async def weather(request: Request):
    try:
        ip = request.client.host
        logger.info(f"Request from ip: {ip}")
        lat, lon = await ip_to_loc(ip)
        weather_response = await openweather(lat, lon)
        json_resp = await makeresponse(weather_response)
        logger.info(f"Send response for ip {ip}, city {json_resp.get('city')}")
        return JSONResponse(json_resp)
    except Exception as e:
        logger.exception("Error in main func", e)
