import os

import requests


path = './books'
with open('filestreem.txt') as file_streem:
    os.makedirs(path, exist_ok=True)
    os.chdir(path)
    for index, line_streem in enumerate(file_streem):
        response = requests.get(line_streem)
        response.raise_for_status() 
        filename = f'id{index+1}.txt'
        with open(filename, 'wb') as file:
            file.write(response.content)