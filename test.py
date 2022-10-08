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
