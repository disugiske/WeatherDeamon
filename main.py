import logging
import sys
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from utils import ip_to_loc, openweather

app = FastAPI()


@app.get("/", response_class=JSONResponse)
async def weather(request: Request):
    ip = request.client.host
    lat, lon = await ip_to_loc(ip)
    return JSONResponse(await openweather(lat, lon))