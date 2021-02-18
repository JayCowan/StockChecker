import requests
import const
from bs4 import BeautifulSoup


def overclockers_check(link):
    return_link = requests.get(link, const.HEADERS)
    if return_link.status_code != 200:
        print(return_link.status_code + " on overclockers.co.uk")
    soup = BeautifulSoup(return_link.content, 'html.parser')
    result = soup.find('div', class_='bottom')
    stock_elems = result.find('div', class_='detail_quantity_label')
    try:
        elems = stock_elems['data-instock-amount']
        if elems == '0':
            return const.NOT_IN_STOCK
        else:
            title = soup.find('meta', property='og:title')
            print(title['content'])
            return {
                "title": title['content'],
                "stock": stock_elems['data-instock-amount'],
                "link": link
            }
    except:
        return const.NOT_IN_STOCK
