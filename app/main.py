from fastapi import FastAPI
from config import config
from router.endpoints import api_router


app = FastAPI(
    title=config.PROJECT_NAME, 
    openapi_url=f"{config.API_PREFIX}/openapi.json",
    version=config.VERSION,
    debug=config.DEBUG
    )

app.include_router(api_router,prefix=config.API_PREFIX)

@app.get("/")
def root():
    return {"message": "Hello World"}




