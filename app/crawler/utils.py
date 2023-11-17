import json
from typing import List, TextIO
import csv
import pandas as pd

def json_saver(data_response:str,name_file:str) -> None:
    formated_name=name_file.replace(' ', '_').lower()

    open(f'app/data/negras/{formated_name}.json', 'w').write(json.dumps(data_response))
    
def generate_url(name:str,type_search:int,page:int=1)->str:
    processed_name=name.replace(" ","+")
    
    if type_search == 1:
        return f"https://www.jusbrasil.com.br/pecas/busca?q=\"{processed_name}\"&p={page}"
    
    elif type_search == 2:
        return f"https://www.jusbrasil.com.br/jurisprudencia/busca?q=\"{processed_name}\"&p={page}"
    
def get_names(person_color:str,analised_row:str,wanted_row:str,delimiter:str) -> List[str]:
    
    input_file=f'app/data/input/docentes.csv'
    df = pd.read_csv(input_file,delimiter=delimiter)
     
    nomes = df.loc[df[analised_row]==person_color,wanted_row].tolist()
        
    print(f'Listando nomes de pessoas que se identificam com a cor {person_color}')
    return nomes


print(get_names(person_color='Negra',analised_row='COR',wanted_row='NOME',delimiter='|'))

