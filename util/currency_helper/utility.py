import logging
from cache.cache import Cache
from model.currency import Currency
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

def getCurrencies():
    try:
        with open('data/currencies') as curfile:
            for line in curfile.readlines():
                row=line.split('\t')
                c=Currency(symbol=row[0], name=row[1].split('\n')[0])
                Cache.currencies[c.symbol]=c
    except Exception as ex:
        logging.error('here %s' %str(ex))

def list_all_currencies():
    for k, v in Cache.currencies.items():
        logging.info('%s %s %s' %(v.symbol, v.name, v.price))