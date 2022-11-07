import logging
import sys
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from utils import ip_to_loc, openweather

logger = logging.getLogger('Weather')

logging.basicConfig(
        filename="weather.log",
        encoding="UTF-8",
        filemode="w",
        format="[%(asctime)s] %(levelname).1s %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        level= logging.INFO
    )
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname).1s %(message)s"))
logger.addHandler(handler)

app = FastAPI()
@app.get("/", response_class=JSONResponse)
async def weather(request: Request):
    ip = request.client.host
    lat, lon = await ip_to_loc(ip)
    return JSONResponse(await openweather(lat, lon))