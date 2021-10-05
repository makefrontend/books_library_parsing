import os

import requests


def check_for_redirect(response):
    if response.history:
        raise requests.HTTPError


with open('filestreem.txt') as books_url:
    path = './books'
    os.makedirs(path, exist_ok=True)
    os.chdir(path)
    for index, book_url in enumerate(books_url):
        response = requests.get(book_url)
        try:
            response.raise_for_status()
            check_for_redirect(response)
        except:
            print(f'Книги c id{index+1} не найдено! Пропускаем!')
            continue
        filename = f'id{index+1}.txt'
        with open(filename, 'wb') as file:
            file.write(response.content)
print('Парсинг завершен!')