from crawler import api as crawler_api
from matcher import api as matcher_api

from fastapi import APIRouter

api_router=APIRouter()

api_router.include_router(crawler_api.router, prefix="/crawler", tags=['crawler'])
api_router.include_router(matcher_api.router, prefix="/matcher", tags=['matcher'])