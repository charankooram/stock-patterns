import logging
from cache.cache import Cache
from model.crypto import Crypto
from bs4 import BeautifulSoup
import requests
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

def get_cryptos():
    def __map(list):
        new_list=[]
        for l in list:
            new_list.append(l.string)
        return new_list
    url = 'https://coinmarketcap.com/all/views/all/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    logging.debug('fetched data from coinmarketcap %s' %(page))

    slist = __map(soup.find_all("span", class_='currency-symbol visible-xs'))
    nlist = __map(soup.find_all("a", class_='currency-name-container link-secondary'))
    plist = __map(soup.find_all("a", class_='price'))

    logging.debug('populating cache')
    pointer = 0
    for s in slist:
        n = nlist[pointer]
        p = plist[pointer]
        Cache.cryptos[s] = Crypto(symbol=s, name=n, price=p)
        pointer += 1

def list_all_cryptos():
    cryptos = Cache.cryptos
    for c in sorted(cryptos.values(), reverse=True):
        logging.info('%s' %str(c))