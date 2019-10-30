class Currency:

    def __init__(self, symbol, name):
        self.symbol=symbol
        self.name=name
        self.price=0.0

    def set_price(self, price):
        self.price=price
