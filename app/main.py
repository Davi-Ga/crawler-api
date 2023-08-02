from fastapi import FastAPI
from config import config
from router.endpoints import api_router
from crawler.exceptions import JurisprudenceNotFoundException,InternalServerException
from fastapi.responses import JSONResponse
from fastapi import Request
from crawler.handlers import internal_server_error_handler,jurisprudence_not_found_handler

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

app.add_exception_handler(InternalServerException, internal_server_error_handler)
app.add_exception_handler(JurisprudenceNotFoundException, jurisprudence_not_found_handler)

