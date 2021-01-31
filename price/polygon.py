from polygon import RESTClient, STOCKS_CLUSTER

class Api:
    def __init__(self, config):
        self.client = RESTClient(config['api_key'])

    def get_price(self, symbol):
        response = self.client.stocks_equities_last_quote_for_a_symbol(symbol)
        print(response)
