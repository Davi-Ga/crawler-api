from fastapi import APIRouter
from crawler.core import get_jurisprudences
from .exceptions import JurisprudenceNotFoundException,InternalServerException
from fastapi.responses import JSONResponse
from fastapi import Request
from .writer import csv_writer
import json

router=APIRouter()

@router.get('/search/{name}')
async def jurisprudences(name:str):
    
    if data := await get_jurisprudences(name):
        data_json=json.dumps(data)
        csv_writer(json_string=data_json,name_file=name)
        return JSONResponse(data)
    else:
        raise JurisprudenceNotFoundException(name=name)


