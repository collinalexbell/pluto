from brokers import tdameritrade
import keys
from sell import SellLimit

client = tdameritrade.Client(keys.broker)
accounts = client.get_accounts()

for i, act in enumerate(accounts):
    print(f"{i}: {act}")
act = int(input("Select an account index:"))
if act < 0 or act >= len(accounts):
    print("ERROR: select a valid act")
    exit(-1)
positions = client.get_positions(accounts[act].act_num)
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
        sell_lim_position = SellLimit(symbol, price, shares)

if sell_lim_position is None:
    print("You don't own that stock.")
    exit(-1)

print(f"{sell_lim_position} is set.")
print("starting price monitor")

while(get_cur_price(symbol) < sell_lim_position.price):
    time.sleep(30)
client.sell(sell_lim_position)
