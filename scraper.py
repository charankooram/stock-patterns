import requests
import lxml.html
import logging

class Scraper():
    def __init__(self, src_url, regex):
        self.src_url = src_url
        self.regex = regex
    def get_quote(self, symbol):
        try:
            response = requests.get("{}/{}".format(self.src_url,symbol))
        except Exception as e:
            logging.error(str(e))
        html_text = response.text
        doc = lxml.html.document_fromstring(html_text)
        el = doc.xpath("//span[@class='{}']".format(self.regex))
        if len(el) == 0:
            return None
        quote = el.pop().text
        return quote





