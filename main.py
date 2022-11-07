import httpx
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

app = FastAPI()
@app.get("/", response_class=JSONResponse)
def weather(request: Request):
    #response = httpx.get()
    client_host = request.client.host
    return JSONResponse(client_host)