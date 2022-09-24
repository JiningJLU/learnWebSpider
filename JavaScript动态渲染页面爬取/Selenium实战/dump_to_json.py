import json
from os import mkdir
from os.path import exists
RESULT_DIR = 'results'


def save_data(data):
    if not exists(RESULT_DIR):
        mkdir(RESULT_DIR)
    name = data.get('name')
    data_path = f'{RESULT_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=4)