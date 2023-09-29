import json

def json_saver(data_response:str,name_file:str) -> None:
    open(f'{format_name_file(name_file)}.json', 'w').write(json.dumps(data_response))
    
def format_name_file(name_file:str) -> str:
    return name_file.replace(' ', '_').lower()