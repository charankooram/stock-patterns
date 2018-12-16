import csv
import requests
import argparse
import logging
import time
import threading
import concurrent.futures
from data_vendors import AlphaVantage
from data_vendors import IEXTrading
from data_vendors import YahooFinance
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

"""
    Read from the csv file in the project folder
    and extract all the symbol names from the first column
    of this csv file.
"""
def getNASDAQsymbols():
    nyse = []
    try:
        with open('companylist.csv') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            line = 0
            for row in csv_reader:
                if line > 0:
                    nyse.append(row[0])
                line += 1
    except Exception as ex:
        logging.error(str(ex))
    return nyse




def main(key):
    nasdaqSymbols=getNASDAQsymbols()
    start_time = time.time()
    sum = 0.0

    #for symbol in nasdaqSymbols:
        #alpha_exchange.readStockData(symbol, key)
        #iex_trading.readStockData(symbol)
        #if not (('^' in symbol) or ('.' in symbol)):
            #value_of_symbol=yahoo_finance.readStockData(symbol.strip())
            #sum += float(value_of_symbol)
        #logging.debug("currently taken {} mins for sum {}".format((time.time() - start_time)/60, str(sum)))

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        future_to_symbol_value = {executor.submit(yahoo_finance.readStockData, sym) for sym in nasdaqSymbols}
        for future in concurrent.futures.as_completed(future_to_symbol_value):
            symbol_value=future_to_symbol_value[future]
            try:
                data = future.result()
            except Exception as ex:
                logging.error(str(ex))
            else:
                logging.info("{}-{}".format(symbol_value, data))

    end_time = time.time()
    logging.info("took {} mins for {}".format(str((end_time-start_time)/60)), str(sum))







if __name__ == "__main__":
    logging.info("Identify NASDAQ symbols passing ERBO pattern")
    alpha_exchange = AlphaVantage()
    iex_trading = IEXTrading()
    yahoo_finance= YahooFinance()
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="Enter api-key for alpha avantage api access")
    args=parser.parse_args()
    main(args.key)

