from alpha_vantage.timeseries import TimeSeries
class Api:
    def __init__(self, config):
        self.client = TimeSeries(key=config['api_key'])

    def get_price(self, symbol):
        price = float(self.client.get_quote_endpoint(symbol)[0]['05. price'])
        print(price)
        return price

