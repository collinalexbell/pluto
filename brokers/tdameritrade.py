from td.client import TDClient

class Client:

    def __init__(self, td_config):
        # Create a new session, credentials path is required.
        TDSession = TDClient(
            client_id=td_config['client_id'],
            redirect_uri=td_config['redirect_uri'],
            credentials_path='/home/kuberlog/.secrets/tdameritrade'
        )

        # Login to the session
        TDSession.login()

