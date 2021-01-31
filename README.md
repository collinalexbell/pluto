# pluto
For when your broker doesn't let you set a $69,420 sell limit.

Using free API keys, you can check the market every minute for the trigger price. If you want a faster response time, you can either pay Alpha Advantage for more throughput or you can implement another price consumer.

## Setup
First, run `pip install -r requirements.txt`
You need to copy `keys.py.example` to `keys.py` and fill out everyting in `<>` with your own keys.

### TD Ameritrade Key
You can get a TD Ameritrade Key [here](https://developer.tdameritrade.com/).
After creating an account, go to "My Apps" and create a new one. 
The `client_id` in the key file is actually the `Consumer Key` in your app description.

### Alpha Advantage
Go [here](https://www.alphavantage.co/) and get your free key. 

## Usage
`python main.py`

Note: items in bold are inputs you type and press enter for

<pre>
kuberlog@pop-os:~/code/pluto$ python main.py 
0: <YOUR ACT NUM SHOWN HERE> @ $800.0
Select an account index: <b>0</b>
0: MMDA1 w/ 800.0 shares
1: GME w/ 2.0 shares
Enter the symbol of the stock to sell limit: <b>GME</b>
Enter the price to sell: <b>69420</b>
Enter the shares to sell: <b>1</b>
SellLimit on GME of 1.0 shares at price 325.0 is set.
starting price monitor
</pre>
