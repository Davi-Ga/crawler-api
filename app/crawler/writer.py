import csv
import json

def csv_writer(json_string:str, name_file:str) -> csv.DictWriter:
    data = json.loads(json_string)
    headers = data[0].keys()
    
    with open(f'data/{name_file}.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
