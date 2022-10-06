import requests
from bs4 import BeautifulSoup

for count in range(1, 287):

    url = f'http://www.noyantapan.am/catalog/books/?PAGEN_1={count}'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('div', class_='item product sku')
    for items in data:
        name = items.find('span', class_='middle').text
        price = items.find('a', class_='price').text
        article = 'http://www.noyantapan.am' + items.find('a', class_='picture').get('href')
        print(name, price, article, sep='\n')
