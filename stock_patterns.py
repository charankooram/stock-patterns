import csv
import requests
import argparse
import logging
from data_vendors import AlphaVantage
from data_vendors import IEXTrading
from data_vendors import YahooFinance
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

"""
    Read from the csv file in the project folder
    and extract all the symbol names from the first column
    of this csv file.
"""
def getNYSEsymbols():
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
    nyseSymbols=getNYSEsymbols()
    for symbol in nyseSymbols:
        #alpha_exchange.readStockData(symbol, key)
        #iex_trading.readStockData(symbol)
        yahoo_finance.readStockData(symbol)






if __name__ == "__main__":
    logging.info("Identify NYSE symbols passing ERBO pattern")
    alpha_exchange = AlphaVantage()
    iex_trading = IEXTrading()
    yahoo_finance= YahooFinance()
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="Enter api-key for alpha avantage api access")
    args=parser.parse_args()
    main(args.key)

