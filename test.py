# test 1

import requests
from bs4 import BeautifulSoup
import csv


class Book:
    def __init__(self, title, summary):
        self.title = title
        self.summary = summary


def get_next_page(response):
    soup = BeautifulSoup(response.text, "lxml")
    tie = soup.find('li', class_="bx-pag-next").find('a')
    return str() if tie == None else "http://www.noyantapan.am" + tie.get('href')


def parse_book(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    title = soup.find('h1', class_='changeName').text

    table = soup.find('table', class_='stats').find_all('tr', class_='gray')
    summary = {card.find('td').text: card.find_all('td')[1].text.strip() for card in table}
    print(title)

    return Book(title, summary)


books_list = list()

current_page = "http://www.noyantapan.am/catalog/books/?PAGEN_1=1"
while current_page:
    response = requests.get(current_page)
    soup = BeautifulSoup(response.text, "lxml")

    item_products = soup.find('div', class_='items productList')
    cards = item_products.find_all('div', class_='item product sku')
    for card in cards:
        books_list.append(parse_book("http://www.noyantapan.am" + card.find('a', class_='name').get('href')))

    current_page = get_next_page(response)

column_set = set()
for book in books_list:
    for key in book.summary.keys():
        column_set.add(key)
column_list = [*column_set]

with open('noyantapan.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(column_list)

for book in books_list:
    with open('noyantapan.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([book.summary.get(decisive) for decisive in column_list])



# test 2
import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}


def get_data():
    with open('zangak.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'title',
                'author',
                'publisher',
                'price',
                'language',
                'pages',
                'genre',
                'category',
                'target',
                'EAN',
                'code',
                'year',
                'url'

            )
        )
    for page in range(1, 920):
        url = f'https://zangakbookstore.am/grqer?page={page}'
        response  = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('div', class_='row no-gutters product-items-list items-list-container')
        cards = data.find_all('div', class_='col-6 col-md-4 col-lg-6 col-xl-4 col-xxl-3 mb-5 list-item')
        for c_url in cards:
            cards_url = c_url.find('a', class_='d-inline-block position-relative').get('href')
            yield cards_url


for card_url in get_data():
    response = requests.get(card_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    try:
        title = soup.find('h1', class_='product-name mb-4 d-none d-md-block').text
    except:
        title = ''
    print(title)
    try:
        price = soup.find('div', class_='product-price-view mb-2').text
    except:
        price = ''
    try:
        author = soup.find('a', class_='color-main text-decoration-none author-btn').text
    except:
        author = ''
    try:
        found = soup.find('div', id='tab_details', class_='tab-pane fade show active')
        if found == None:
            found = soup.find('div', id='tab_details', class_='tab-pane fade ')
        table = soup.find_all('div', class_='form-row')
    except:
        table = ''
    try:
        summary = [couple.find_all('div')[1].text for couple in table]
    except:
        summary = ''
    try:
        publisher = summary[0]
    except:
        publisher = ''
    try:
        language = summary[4]
    except:
        language = ''
    try:
        pages = summary[6]
    except:
        pages = ''
    try:
        cover = summary[5]
    except:
        cover = ''
    try:
        genre = soup.find_all('li', class_='breadcrumb-item')[1].text
    except:
        genre = ''
    try:
        category = soup.find_all('li', class_='breadcrumb-item')[2].text
    except:
        category = ''
    try:
        target = summary[9]
    except:
        target = ''
    try:
        EAN = summary[1]
    except:
        EAN = ''
    try:
        code = summary[2]
    except:
        code = ''
    try:
        year = summary[3]
    except:
        year = ''
    try:
        book_url = card_url
    except:
        book_url = ''
    with open('zangak.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                title,
                author,
                publisher,
                price,
                language,
                pages,
                genre,
                category,
                target,
                EAN,
                code,
                year,
                book_url

            )
        )

# test 3
import requests
from bs4 import BeautifulSoup
import csv
import sys

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}


def get_data():
    with open('zangak.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'title',
                'author',
                'publisher',
                'price',
                'language',
                'pages',
                'genre',
                'category',
                'target',
                'EAN',
                'code',
                'year',
                'url'

            )
        )
    for page in range(1, 20):
        url = f'https://zangakbookstore.am/grqer?page={page}'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('div', class_='row no-gutters product-items-list items-list-container')
        cards = data.find_all('div', class_='col-6 col-md-4 col-lg-6 col-xl-4 col-xxl-3 mb-5 list-item')
        for c_url in cards:
            cards_url = c_url.find('a', class_='d-inline-block position-relative').get('href')
            yield cards_url


for card_url in get_data():
    response = requests.get(card_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    try:
        title = soup.find('h1', class_='product-name mb-4 d-none d-md-block').text
        print(title)

        price = soup.find('div', class_='product-price-view mb-2').text
        try:
            author = soup.find('a', class_='color-main text-decoration-none author-btn').text
        except:
            author = str()

        found = soup.find('div', id='tab_details', class_='tab-pane fade show active')
        if found == None:
            found = soup.find('div', id='tab_details', class_='tab-pane fade ')
        table = soup.find_all('div', class_='form-row')

        summary = [couple.find_all('div')[1].text for couple in table]

        publisher, EAN, code, year, language, cover, pages = summary[:7]

        genre = soup.find_all('li', class_='breadcrumb-item')[1].text
        category = soup.find_all('li', class_='breadcrumb-item')[2].text
        target = summary[9]
        book_url = card_url
    except:
        print(card_url, file=sys.stderr)
        continue

    with open('zangak.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                title,
                author,
                publisher,
                price,
                language,
                pages,
                genre,
                category,
                target,
                EAN,
                code,
                year,
                book_url

            )
        )
