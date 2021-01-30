class Position:
    def __init__(self, symbol, qnty):
        self.symbol = symbol
        self.quantity = qnty

    def __repr__(self):
        return f"{self.symbol} w/ {self.quantity} shares"
