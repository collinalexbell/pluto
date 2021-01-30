
class SellLimit:
    def __init__(self, symbol, price, quantity):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"SellLimit on {self.symbol} of {self.quantity} shares at price {self.price}"
