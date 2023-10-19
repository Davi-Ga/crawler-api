from fastapi import APIRouter, File, UploadFile, HTTPException
import json
from typing import Annotated
from .core import readJSON, readPDF, readTXT

router=APIRouter()

@router.post('/search_file/')
async def reader(file: UploadFile = File(..., description="Enviar Json do tipo \n{\n['title': 'etc...',\n 'body': '...']}",), words_bag: UploadFile = File(..., description="Enviar um arquivo TXT com as palavras a serem analisadas Ex: provimento\\n negar provimento (uma palavra em cada linha)")):


    file_content_type = file.content_type
    file.file.seek(0,2)
    file_size = file.file.tell()
    file.file.seek(0)
 

    words_bag_type = words_bag.content_type
    words_bag.file.seek(0,2)
    words_bag_file_size  = words_bag.file.tell()
    words_bag.file.seek(0)
    
    
    if file_content_type  not in ["application/json", "text/plain"] and words_bag_type not in ["text/plain"]:
        return HTTPException(status_code=400, detail="Invalid Type in !!!")
    
    if file_size and words_bag_file_size <= 0:
        return HTTPException(status_code=400, detail="File is Empty!!!")     


    if file_content_type == "application/json":
            data = json.load(file.file)
            return await readJSON(data, words_bag)
    
    elif file_content_type == "text/plain":
            return readTXT(file, words_bag)



