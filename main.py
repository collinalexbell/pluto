from brokers import tdameritrade
import keys

client = tdameritrade.Client(keys.broker)
accounts = client.get_accounts()
for i, act in enumerate(accounts):
    print(f"{i}: {act}")
input("Select an account:")
