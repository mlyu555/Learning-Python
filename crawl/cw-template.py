import requests
from bs4 import BeautifulSoup
import sys

test_url = 'https://www.haojob123.com/zhichang/cizhixin/4762.html'

def get_html_content(url)-> bytes:
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception('req error')
    return r.content


def parser(html_content: bytes):
    html_encoding = 'gb2312'
    soup = BeautifulSoup(html_content.decode(html_encoding), 'html.parser')

    content = soup.find('div', class_='main').find('div', class_='content')
    temp = soup.get_text()
    print(temp)


if __name__ == '__main__':
    html_content = get_html_content(test_url)
    parser(html_content)
