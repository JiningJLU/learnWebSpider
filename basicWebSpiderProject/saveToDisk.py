import json
from os import makedirs
from os.path import exists

RESULTS_DIR = 'results'
# 比较精巧，利用了逻辑或的短路
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)


def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    # ensure_ascii表示 中文是用unicode展示还是用中文字符本身展示
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)