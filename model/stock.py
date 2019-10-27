class Stock:

    def __init__(self, symbol, name, lastsale, marketcap, ipoyear, sector, industry, summary):
        self.symbol=symbol
        self.name=name
        self.lastsale=lastsale
        self.marketcap=marketcap
        self.ipoyear=ipoyear
        self.sector=sector
        self.industry=industry
        self.summary=summary
        self.price=0.0

    def set_price(self, price):
        self.price=price
