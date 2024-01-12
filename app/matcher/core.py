import json
from fastapi import File, UploadFile, HTTPException
from fastapi.responses import FileResponse

from PyPDF2 import PdfReader
import re
import io, os 
import pandas as pd




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
        file = file.lower()

        for word in word_bags:
            word = word.decode('utf-8')
            word=word.replace('\r\n', '')

            if re.search(word, file):
                result.append(word)


    if result:
        return {"type": "Julgamento Concluido!!!" ,
                "response": result}
    else:
        return {"type": "Julgamento em Andamento!!!",
                "response": result}



async def readCsv(file: UploadFile = File(...), words_bag: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)
        data = df["Original_Text"].str.lower()

        result = []
        label = []
        word_bags = words_bag.file.readlines()

        for i in range(len(df)):
            aux = []
            for word in word_bags:
                word = word.decode('utf-8')
                word=word.replace('\r\n', '')

                if isinstance(data[i], float):
                    continue

                elif re.search(word, data[i]):
                    result.append(word)
                    aux.append("Fechado")
                else:
                    aux.append("Aberto")
                print(result)

            if "Fechado" in aux:
                label.append("Fechado")
            else:
                label.append("Aberto")

        print(df)
        df["Label"] = label
                
        # Save the updated DataFrame to a new CSV file
        updated_file_path = 'updated_file.csv'
        df.to_csv(updated_file_path, index=False)

        if result:
            return FileResponse(updated_file_path, media_type="text/csv", filename="updated_file.csv")

        else:
            return {"type": "Julgamento em Andamento!!!",
                    "response": result}
 
 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def collector(file: UploadFile = File(...), grupo:str = "" ):
    print(file)


    # Specify the directory path
    directory_path = f"./data/{grupo}"

    # Fazer um lista de todos os documentos da pasta
    files = os.listdir(directory_path)
    data = []
    header = ["Name", "Original_Text", "Label"]

    # Pegar um documento por vezes
    for file in files:
        name = os.path.splitext(file)[0]
        name = remove_special_characters(name)

        path_file = f'{directory_path}/{file}'
        if(os.path.getsize(path_file) <= 2):
            continue
        else:
            with open(path_file, 'r') as f:
                print(f"{path_file}")
                original_text = json.load(f)

                for petition in original_text:
                    try:    
                        text = petition["body_petition"]
                        data.append([f"{name}", f"{text}", f"None"])
                    except: 
                        pass    

    collection = pd.DataFrame(data, columns=header)
    collection.to_csv(f"./data/Coleta_{grupo.title()}.csv", index=False) 
