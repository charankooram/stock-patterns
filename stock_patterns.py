import time
import configparser
from data_vendors import AlphaVantage
from data_vendors import IEXTrading
from data_vendors import YahooFinance
from util.stock_helper.utility import *
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def main(vendor):
    """
        Read from the companies list and fetch the quotes for
        these stickers from the given vendor and do tasks from
        the utility module with these stock information.
    """
    getNYSEsymbols()
    start_time=time.time()
    for symbol, stock in Cache.stocks.items():
        if '^' in symbol or \
           '.' in symbol or \
           ' ' in symbol:
            continue
        try:
            price=vendor.readStockData(symbol)
            stock.set_price(price)
            if price < 20:
                print(stock)
        except Exception as price_exc:
            logging.error('could not fetch %s - %s' %(symbol, str(price_exc)))
        time.sleep(0.01)  # control the load on vendor between requests.
    end_time=time.time()
    logging.info('%s mins to process %d stocks' %((end_time-start_time)/60,len(Cache.stocks)))
    list_all_sectors()


if __name__ == "__main__":
    config=configparser.ConfigParser()
    config.read('config/conf.ini')
    vendor_param=config['source']['stock_vendor']
    threshold_param=config['threshold']['value']
    key_param=config['alpha']['key']
    logging.info("Identify NYSE symbols < %s" %threshold_param)
    vendor=None
    if vendor_param == 'yahoo':
        vendor=YahooFinance()
    elif vendor_param == 'alpha':
        vendor=AlphaVantage(key_param)
    else:
        vendor=IEXTrading()

    logging.debug(vendor)
    main(vendor)

