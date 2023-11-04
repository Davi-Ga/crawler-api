import json
from typing import List, TextIO
import csv
import pandas as pd

def json_saver(data_response:str,name_file:str) -> None:
    open(f'app/data/pardas/{format_name_file(name_file)}.json', 'w').write(json.dumps(data_response))
    
def format_name_file(name_file:str) -> str:
    return name_file.replace(' ', '_').lower()

def generate_url_jurisprudence(name:str,page:int=1)->str:
    processed_name=name.replace(" ","+")
    return f"https://www.jusbrasil.com.br/jurisprudencia/busca?q=\"{processed_name}\"&p={page}"

def generate_url_procedural_parts(name:str,page:int=1)->str:
    processed_name=name.replace(" ","+")
    return f"https://www.jusbrasil.com.br/pecas/busca?q={processed_name}&p={page}"

def get_names(person_color:str,analised_row:str,wanted_row:str,delimiter:str) -> List[str]:
    
    input_file=f'app/data/input/professores_ufop.csv'
    df = pd.read_csv(input_file,delimiter=delimiter)
     
    nomes = df.loc[df[analised_row]==person_color.upper(),wanted_row].tolist()
        
    print(f'Listando nomes de pessoas que se identificam com a cor {person_color}')
    return nomes

print(get_names(person_color='parda',analised_row='raca',wanted_row='Nome_do_Servidor',delimiter=';'))