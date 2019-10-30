from util.currency_helper.utility import *
from data_vendors import YahooFinance
import time

def main(vendor):
    getCurrencies()
    start_time=time.time()
    for symbol, currency in Cache.currencies.items():
        try:
            price=vendor.readCurrencyData(symbol)
            currency.set_price(price)
        except Exception as price_exc:
            logging.error('could not fetch %s - %s' %(symbol, str(price_exc)))
        time.sleep(0.01)  # control the load on vendor between requests.
    end_time=time.time()
    logging.info('%s mins to process %d stocks' %((end_time-start_time)/60,len(Cache.currencies)))
    list_all_currencies()
if __name__ == '__main__':

    main(vendor=YahooFinance())