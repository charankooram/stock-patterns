import requests
import logging
from scraper import Scraper

"""
    Scrape quotes directly from Yahoo Finance Web Portal.
"""
class YahooFinance():
    def __init__(self):
        pass
    def readStockData(self, symbol):
        scraper=Scraper(src_url='https://finance.yahoo.com/quote',regex='Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)')
        price=scraper.get_quote(symbol)
        logging.info("price for {} is {}".format(symbol,price))
"""
    15 min delayed quotes from all symbols not
    recently used by IEX traders.
"""
class IEXTrading():
    def __init__(self):
        pass
    def readStockData(self, symbol):
        url = "https://api.iextrading.com:443/1.0/stock/{}/chart/1d".format(symbol.lower())
        response = requests.get(url=url)
        logging.info(response.json()[0])

"""
    Free Version of the api-key only allows querying 5 requests per minute.
    Premium membership required for greater api usage.
"""
class AlphaVantage():
    def __init__(self):
        pass
    """
        Given an NYSE symbol, use alpha api to get 
        stock price data.
    """
    def readStockData(self, symbol, key):
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": "1min",
            "apikey": key
        }
        resp=requests.get(url, params)
        logging.info(resp.json())
