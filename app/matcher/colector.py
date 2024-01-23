import os, re, sys
import pandas as pd
import json


def remove_special_characters(text):
    # Substituir caracteres especiais por espaços em branco
    cleaned_text = re.sub(r'[^a-zA-Z0-9á-úç\.\s]', ' ', text)
    cleaned_text = cleaned_text.title()
    return cleaned_text



# Specify the directory path
grupo = sys.argv[1]
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

