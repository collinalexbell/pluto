import yfinance as yf

def get_price(symbol):
    ticker = yf.Ticker(symbol)
    print(ticker.info['regularMarketPrice'])
    return ticker.info['regularMarketPrice']
