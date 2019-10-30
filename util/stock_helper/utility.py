import csv
import logging
from cache.cache import Cache
from model.stock import Stock
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

"""
    Read from the csv file in the project folder
    and extract all the symbol names from the first column
    of this csv file.
"""
def getNYSEsymbols():
    try:
        with open('data/nysecompanylist.csv') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            line = 0
            for row in csv_reader:
                if line > 0:
                    Cache.stocks[row[0]]=Stock(symbol=row[0],
                        name=row[1],
                        lastsale=row[2],
                        marketcap=row[3],
                        ipoyear=row[4],
                        sector=row[5],
                        industry=row[6],
                        summary=row[7]
                          )

                line += 1
    except Exception as ex:
        logging.error(str(ex))

def list_all_sectors():
    sectors={}
    for symbol, stock in Cache.stocks.items():
        if stock.sector not in sectors():
            sectors[stock.sector]=None
    logging.info(sectors.keys())

