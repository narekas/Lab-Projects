import os
import time

import requests
from bs4 import BeautifulSoup


def get_all_pages():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }

    # request = requests.get(url='http://www.noyantapan.am/catalog/books/', headers=headers)

    # if not os.path.exists('data1'):
    #    os.mkdir('data1')

    # with open('data1/page_1.html', 'w') as file:
    #    file.write(request.text)

    with open('data1/page_1.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    pages_count = int(soup.find('div', class_='bx-pagination-container row').find_all('a')[-2].text)

    for page in range(1, pages_count + 1):
        url = f'http://www.noyantapan.am/catalog/books/?PAGEN_1={page}'

        r = requests.get(url=url, headers=headers)

        with open(f'data1/page_{page}.html', 'w') as file:
            file.write(r.text)

        time.sleep(2)
    return pages_count + 1


def main():
    get_all_pages()


if __name__ == '__main__':
    main()
