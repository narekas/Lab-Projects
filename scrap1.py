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
        table = soup.find('div', class_='tab-pane fade show active').find_all('div', class_='form-row')
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
