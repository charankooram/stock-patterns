import requests
import lxml.html
import logging

class Scraper():
    def __init__(self, src_url, regex):
        self.src_url = src_url
        self.regex = regex

    def get_currency_quote(self, symbol):
        try:
            response=requests.get("{}/{}=X?p={}=X".format(self.src_url, symbol, symbol))
        except Exception as e:
            logging.error('currency not fetched due to %s' %str(e))
        html_text = response.text
        doc = lxml.html.document_fromstring(html_text)
        s1 = "//span[@class='Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)']"
        el = doc.xpath(s1)
        quote = el.pop().text
        return quote
    def get_stock_quote(self, symbol):
        try:
            response = requests.get("{}/{}".format(self.src_url, symbol))
        except Exception as e:
            logging.error('currency not fetched due to%s' %str(e))
        html_text = response.text
        doc = lxml.html.document_fromstring(html_text)
        s1="//span[@class='Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)']"
        el = doc.xpath(s1)
        quote = el.pop().text
        return quote





