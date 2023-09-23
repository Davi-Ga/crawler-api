from fastapi import FastAPI
from config import config_api
from router.endpoints import api_router

app = FastAPI(
    title=config_api.PROJECT_NAME, 
    openapi_url=f"{config_api.API_PREFIX}/openapi.json",
    version=config_api.VERSION,
    debug=config_api.DEBUG
    )

app.include_router(api_router,prefix=config_api.API_PREFIX)
