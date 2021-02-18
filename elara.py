import requests
import const
from bs4 import BeautifulSoup

def check(link):
    return_link = requests.get(link, const.HEADERS)
    if return_link.status_code != 200:
        print(return_link.status_code + " on elara.ie")
    soup = BeautifulSoup(return_link.content, 'html.parser')
    result = soup.find('div', class_='prodetail')
    try:
        stock_elem = result.find('span', id='ctl00_ContentPlaceHolder1_lblStock')
        if stock_elem.contents[0] != '0':
            title = soup.find('meta', property='og:title')
            print(title['content'])
            return {
                "title": title['content'],
                "stock": stock_elem.contents[0],
                "link": link
            }
        else:
            return const.NOT_IN_STOCK
    except:
        return const.NOT_IN_STOCK
