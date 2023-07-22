from fastapi import FastAPI
from typing import Union
from config import config

app = FastAPI(
    title=config.PROJECT_NAME, 
    openapi_url=f"{config.API_PREFIX}/openapi.json",
    version=config.VERSION,
    debug=config.DEBUG
    )

@app.get("/")
def root():
    return {"message": "Hello World"}


