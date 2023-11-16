import os, re
import pandas as pd
import json


def remove_special_characters(text):
    # Substituir caracteres especiais por espaços em branco
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    cleaned_text = cleaned_text.title()
    return cleaned_text



# Specify the directory path
directory_path = "./data/"

# Fazer um lista de todos os documentos da pasta
files = os.listdir(directory_path)
data = []
header = ["Name", "Original_Text", "Label"]
# Pegar um documento por vezes
for file in files:
    name = os.path.splitext(file)[0]
    name = remove_special_characters(name)

    path_file = f'./data/brancas/{file}'
    if(os.path.getsize(path_file) <= 2):
        continue
    else:
        with open(path_file, 'r') as f:
            original_text = json.load(f)
            try:
                original_text = original_text[1]["body_petition"]
                data.append([name, original_text, ''])
            except: 
                data.append([name, "None", ''])


collection = pd.DataFrame(data, columns=header)
collection.to_csv("Coleta.csv", index=False) 

