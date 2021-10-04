import os

import requests


path = './books'
with open('filestreem.txt') as books_url:
    os.makedirs(path, exist_ok=True)
    os.chdir(path)
    for index, book_url in enumerate(books_url):
        response = requests.get(book_url)
        response.raise_for_status() 
        filename = f'id{index+1}.txt'
        with open(filename, 'wb') as file:
            file.write(response.content)