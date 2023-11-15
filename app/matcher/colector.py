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

# Get a list of all files in the directory
files = os.listdir(directory_path)
data = []
header = ["Name", "Original_Text", "Label"]
# Print the names of the files
for file in files:
#   print(file)  
    
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
                # print(original_text)
                data.append([name, original_text, ''])
            except: 
                data.append([name, "None", ''])
            # print(data)



collection = pd.DataFrame(data, columns=header)
collection.to_csv("Coleta.csv", index=False) 

