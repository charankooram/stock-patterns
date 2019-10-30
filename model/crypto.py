from functools import total_ordering

class Crypto():

    def __init__(self, symbol, name, price):
        self.symbol=symbol
        self.name=name
        self.price=price.split('$')[1]

    @total_ordering
    def __lt__(self, other):
        return self.price < other.price

    @total_ordering
    def __gt__(self, other):
        return self.price > other.price

    def __str__(self):
        return '%s %s %s' %(self.symbol, self.name, self.price)