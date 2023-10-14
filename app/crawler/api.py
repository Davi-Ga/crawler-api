from fastapi import APIRouter
from .core import get_jurisprudences
from .exceptions import JurisprudenceNotFoundException,InternalServerException
from fastapi.responses import JSONResponse
from .utils import json_saver

router=APIRouter()

@router.get('/search/{name}')
async def jurisprudences(name:str):
    
    if data := await get_jurisprudences(name):
        json_saver(data_response=data,name_file=name)
        
        return JSONResponse(data)
    else:
        raise JurisprudenceNotFoundException(name=name)
    
@router.get('/list-search/{name}')
async def jurisprudences(names:list):
    
    if data := await get_jurisprudences(name):
        json_saver(data_response=data,name_file=name)
        
        return JSONResponse(data)
    else:
        raise JurisprudenceNotFoundException(name=name)



