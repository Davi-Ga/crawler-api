from fastapi import APIRouter, File, UploadFile, HTTPException
import json
from typing import Annotated
from .core import readJSON, readPDF, readTXT, readCsv


router=APIRouter()

@router.post('/search_file/')

async def reader_Json(file: UploadFile = File(..., description="Enviar Json do tipo \n{\n['title': 'etc...',\n 'body': '...']}",), words_bag: UploadFile = File(..., description="Enviar um arquivo TXT com as palavras a serem analisadas Ex: provimento\\n negar provimento (uma palavra em cada linha)")):
    json_data = json.load(file.file)
    file_content_type = file.content_type
    file.file.seek(0,2)
    file_size = file.file.tell()
    file.file.seek(0)
 

    words_bag_type = words_bag.content_type
    words_bag.file.seek(0,2)
    words_bag_file_size = words_bag.file.tell()
    words_bag.file.seek(0)
    
    
    if file_content_type not in ["application/json"] and words_bag_type not in ["text/plain"]:
        return HTTPException(status_code=400, detail="Invalid Type in !!!")
    
    if file_size and words_bag_file_size <= 0:
        return HTTPException(status_code=400, detail="File is Empty!!!")     

 
    data = json.load(file.file)
    return await readJSON(data, words_bag)
    






@router.post("/classificado")
async def reader_Csv(file: UploadFile = File(..., description="Enviar o CSV montado pelo collector para classificar as petições",), words_bag: UploadFile = File(..., description="Enviar um arquivo TXT com as palavras a serem analisadas Ex: provimento\\n negar provimento (uma palavra em cada linha)")):
    csv_file = file

    return await readCsv(csv_file, words_bag)

 