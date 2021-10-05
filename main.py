import os

import requests
from bs4 import BeautifulSoup	
from pathvalidate import sanitize_filename


def check_for_redirect(response):
    if response.history:
        raise requests.HTTPError


def download_txt(url, filename, folder='books/'):
    os.makedirs(folder, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()

    filepath = os.path.join(folder, sanitize_filename(filename) + '.txt')
    with open(filepath, 'wb') as file:
        file.write(response.content)
    return filepath


with open('filestreem.txt') as books_url:
    for book_url in books_url:
        response = requests.get(book_url)
        try:
            response.raise_for_status()
            check_for_redirect(response)
        except:
            print(f'Книги не найдено! Пропускаем!')
            continue
        soup = BeautifulSoup(response.text, 'lxml')
        book_data = soup.find('h1').text.split('::')
        book_title = book_data[0].strip()
        book_author = book_data[1].strip()
        book_link_id = book_url.split('/')[-2].strip('b')
        book_txt_link = f'https://tululu.org/txt.php?id={book_link_id}'
        book_path = download_txt(book_txt_link, book_title)
        print('Заголовок: ', book_title)
        print('Автор: ', book_author)
        print('Путь до книги: ', book_path)
print('Парсинг завершен!')