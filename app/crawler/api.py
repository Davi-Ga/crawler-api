from fastapi import APIRouter
from ..crawler.core import access_page_jurisprudences,access_page_procedural_parts
from .exceptions import JurisprudenceNotFoundException,InternalServerException
from fastapi.responses import JSONResponse
from ..crawler.utils import json_saver

router=APIRouter()

@router.get('/search-jurisprudence/{name}')
async def jurisprudences(name:str):
    
    if data := await access_page_jurisprudences(name):
        json_saver(data_response=data,name_file=name)
        
        return JSONResponse(data)
    else:
        raise JurisprudenceNotFoundException(name=name)
    
@router.get('/search-parts/{name}')
async def procedural_parts(name:str):
    
    if data := await access_page_procedural_parts(name):
        json_saver(data_response=data,name_file=name)
        
        return JSONResponse(data)
    else:
        raise JurisprudenceNotFoundException(name=name)
    
# @router.get('/list-search/{name}')
# async def jurisprudences(names:list):
    
#     if data := await get_jurisprudences(name):
#         json_saver(data_response=data,name_file=name)
        
#         return JSONResponse(data)
#     else:
#         raise JurisprudenceNotFoundException(name=name)



