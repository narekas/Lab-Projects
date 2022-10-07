import requests
from bs4 import BeautifulSoup
from time import sleep

list_card_url = []
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

for page in range(1, 3):
    sleep(1)
    url = f'http://www.noyantapan.am/catalog/books/?PAGE_1=1&PAGEN_1={page}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('div', class_='item product sku')[:30]
    for item in data:
        card_url = 'http://www.noyantapan.am' + item.find('a', class_='name').get('href')
        list_card_url.append(card_url)


for card_url in list_card_url:
    response = requests.get(card_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='mainContainer')
    code = ''.join(data.find('div', class_='propertyTable').text.split())
    print(code)

