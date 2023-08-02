from fastapi import APIRouter
from crawler.core import get_jurisprudences
from .exceptions import JurisprudenceNotFoundException,InternalServerException
from fastapi.responses import JSONResponse
from fastapi import Request

router=APIRouter()

@router.get('/search/{name}')
async def jurisprudences(name:str):
    
    if data := await get_jurisprudences(name):
        return JSONResponse(data)
    else:
        raise JurisprudenceNotFoundException(name=name)


