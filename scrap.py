import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}


def get_data():
    with open('noyantapan.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'title',
                'author',
                'price',
                'language',
                'pages',
                'genre',
                'code',
                'year',
                'url'

            )
        )
    for page in range(1, 286):
        url = f'http://www.noyantapan.am/catalog/books/?PAGEN_1={page}'
        response  = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('div', class_='items productList')
        cards = data.find_all('div', class_='item product sku')
        for c_url in cards:
            cards_url = 'http://www.noyantapan.am' + c_url.find('a', class_='name').get('href')
            yield cards_url


for card_url in get_data():
    response = requests.get(card_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    try:
        title = soup.find('h1', class_='changeName').text
    except:
        title = ''
    print(title)
    try:
        price = soup.find('a', class_='price changePrice').text
    except:
        price = ''
    try:
        table = soup.find('table', class_='stats').find_all('tr', class_='gray')
    except:
        table = ''
    try:
        summary = {card.find('td').text: card.find_all('td')[1].text.strip() for card in table}
    except:
        summary = ''
    try:
        author = summary['Հեղինակ']
    except:
        author = ''
    try:
        language = summary['Լեզու']
    except:
        language = ''
    try:
        pages = summary['Էջերի քանակը']
    except:
        pages = ''
    try:
        genre = soup.find('div', id="breadcrumbs").find_all('li')[6].text
    except:
        genre = ''
    try:
        code = summary['Կոդ']
    except:
        code = ''
    try:
        year = summary['Տարեթիվ']
    except:
        year = ''
    try:
        book_url = card_url
    except:
        book_url = ''
    with open('noyantapan.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                title,
                author,
                price,
                language,
                pages,
                genre,
                code,
                year,
                book_url

            )
        )
