from td.client import TDClient
from account import Account
from position import Position

class Client:

    def __init__(self, td_config):
        # Create a new session, credentials path is required.
        self.session = TDClient(
            client_id=td_config['client_id'],
            redirect_uri=td_config['redirect_uri'],
            credentials_path=td_config['credentials_path']
        )

        # Login to the session
        self.session.login()

    def get_accounts(self):
        accounts = []
        td_accounts = self.session.get_accounts()
        for _, account in enumerate(td_accounts):
            act_num = account['securitiesAccount']['accountId']

            value = account['securitiesAccount']['currentBalances']['liquidationValue']
            accounts.append(Account(act_num, value))

        return accounts

    def get_positions(self, act):
        positions = []
        response = self.session.get_accounts(act, ['positions'])
        position_response = response['securitiesAccount']['positions']
        for _, position in enumerate(position_response):
            symbol = position['instrument']['symbol']
            quantity = position['longQuantity']
            positions.append(Position(symbol, quantity))
        return positions


    def sell(self, sell_limit):
        print("executing {sell_limit})
