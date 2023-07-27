from crawler import api

from fastapi import APIRouter

api_router=APIRouter()

api_router.include_router(api.router,tags=['jurisprudences'])