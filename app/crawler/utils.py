import json
from typing import List,Union

def json_saver(data_response:str,name_file:str) -> None:
    open(f'app/data/{format_name_file(name_file)}.json', 'w').write(json.dumps(data_response))
    
def format_name_file(name_file:str) -> str:
    return name_file.replace(' ', '_').lower()

def generate_url(name:str)->str:
    processed_name=name.replace(" ","+")
    return f"https://www.jusbrasil.com.br/jurisprudencia/busca?q={processed_name}"

def get_names() -> List[str]:
    return ['ABELARD RAMOS FERNANDES', 'ACACIO MANUEL DE CARVALHO', 'ACEVESMORENO FLORES PIEGAZ, ADA MAGALY MATIAS BRASILEIRO']
