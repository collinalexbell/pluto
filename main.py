from brokers import tdameritrade
import keys
import time
from sell import SellLimit
from price import alphaadvantage
from pytz import timezone
from datetime import datetime

client = tdameritrade.Client(keys.broker)
accounts = client.get_accounts()
price_api = alphaadvantage.Api(keys.alpha_advantage)

for i, act in enumerate(accounts):
    print(f"{i}: {act}")
act_ind = int(input("Select an account index:"))
if act_ind < 0 or act_ind >= len(accounts):
    print("ERROR: select a valid act")
    exit(-1)
account = accounts[act_ind]
positions = client.get_positions(account.act_num)
for i, position in enumerate(positions):
    print(f"{i}: {position}")

symbol = input("Enter the symbol of the stock to sell limit: ")
sell_lim_position = None

for i, position in enumerate(positions):
    if position.symbol == symbol:
        price = float(input("Enter the price to sell: "))
        shares = float(input("Enter the shares to sell: "))
        if(shares > position.quantity):
            print(f"You don't own that much of {symbol}")
            exit(-1)
        sell_lim_position = SellLimit(account, symbol, price, shares)

if sell_lim_position is None:
    print("You don't own that stock.")
    exit(-1)

print(f"{sell_lim_position} is set.")
print("starting price monitor")

est = timezone('EST')
def is_market_closed():
    dt = datetime.now(est)
    is_early = dt.hour <= 9 and dt.minute <= 30
    is_late = dt.hour >= 4
    is_weekend = dt.weekday() == 5 or dt.weekday() == 6
    return is_early or is_late or is_weekend

while(is_market_closed() or price_api.get_price(symbol) < sell_lim_position.price):
    time.sleep(60)
client.sell(sell_lim_position)
