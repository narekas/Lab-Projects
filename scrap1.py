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
                'price',
                'author',
                'publisher'
            )
        )
    for page in range(1, 2):
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
    summary = [couple.find_all('div')[1].text for couple in table]
    try:
        publisher = summary[0]
    except:
        publisher = ''
    print(title)

    with open('zangak.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                title,
                price,
                author,
                publisher
            )
        )