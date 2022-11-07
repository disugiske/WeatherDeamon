from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from logger_config import logger
from utils import ip_to_loc, openweather, makeresponse

app = FastAPI()


@app.get("/", response_class=JSONResponse)
async def weather(request: Request):
    ip = request.client.host
    lat, lon = await ip_to_loc(ip)
    weather_response = await openweather(lat, lon)
    json_resp = await makeresponse(weather_response)
    logger.info(f"Send response for ip {ip}")
    logger.exception("Error in main func")
    return JSONResponse(json_resp)