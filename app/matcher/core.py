from PyPDF2 import PdfReader
import re, json, unicodedata
from typing import Annotated
from fastapi import File, UploadFile
import io

def readPDF(file) -> [str, int]:
    """
    READ PDF: função para ler arquivos pdf e converter para texto(string)

    PARAMS: 
        file: PDF FILE = Arquivo PDF a ser lido.

    RETURN 
        clean_text: string = texto limpo limpo (sem escape keys)
        page_num: int = numero de páginas no arquivo
    """

    clean_text = []
    pdf_reader  = PdfReader(open(file, "rb"))
    for page_num in range(len(pdf_reader.pages)):
        text = pdf_reader.pages[page_num].extract_text()
        clean_text.append(text.strip().replace("\n", '').lower())
      

    return clean_text, len(pdf_reader.pages)


def readTXT(file: UploadFile, word_bag: UploadFile):
    """
    READ TXT: função que vai ler o arquivo TXT e procurar se a palavra está presente no arquivo desejado

    PARAMS:
        file: TXT FILE = Arquivo Txt a ser analisado
        pattern: string = Palavra a ser verificada se existe dentro do arquivo

    RETURN:
        NULL
        Printar no console a palavra presente no documento
        
    """
    word_bag = word_bag.file.readlines()
    result = []
    content = file.file.read()

    for word in word_bag:
        word = io.StringIO(word.decode())
        for line in word:
            line = line.split()
            pattern = " ".join(line)
            pattern = pattern.strip()

            if re.search(pattern, content):
                    result.append(pattern)
                

        if result:
            return {"type": "Julgamento Concluido!!!" ,
                    "response": result}
        else:
            return {"type": "Julgamento em Andamento!!!",
                    "response": result}

    # if re.search(r'\b' + re.escape(pattern=pattern) + r'\b', file):
    #     return {"type": "Processo Concluido",
    #             "content": f"{word_bag}"}

    
    # with open(file, "r", encoding="utf-8") as f:
    #     for _, line in enumerate(f, start=1):
    #         line = line.lower()
    #         if pattern in line:
    #             print(f"A palavra {pattern} esta no Documento")
    #             return {"type": "Julgamento Concluido" }
        
    #     f.close()
    # return {"type": "Julgamento em Andamento/ Não Deferido" }


async def readJSON(file_json: dict, words_bag: UploadFile = File(...)) -> object:
    """
    DESCRIPTION:
        READ JSON: função que vai ler o arquivo JSON e procurar se a palavra está presente no arquivo desejado,
          retornando uma mensagem no Console, caso a palavra esteja presente.

    PARAMS:
        file: JSON FILE = Arquivo JSON a ser analisado
        pattern: string = Palavra a ser verificada se existe dentro do arquivo

    RETURN:
        NULL
        Printar no console a palavra presente no documento
    """
    
    result = []
    word_bags = words_bag.file.readlines()
    for i in range(len(file_json)):
        file = file_json[i]['body']

        for word in word_bags:
            word = word.decode('utf-8')
            word=word.replace('\n', '')

            if re.search(word, file):
                result.append(word)

    if result:
        return {"type": "Julgamento Concluido!!!" ,
                "response": result}
    else:
        return {"type": "Julgamento em Andamento!!!",
                "response": result}
