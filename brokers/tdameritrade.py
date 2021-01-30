from td.client import TDClient
from accounts import Account

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

                
