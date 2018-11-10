#this allows me to import my API information from another file
from binance.client import Client
from Bkeys import bkey1
from binance.enums import *
import time
import pprint

api_key = bkey1['api_key']
api_secret = bkey1['api_secret']
client = Client(api_key, api_secret)
class Binance:
    def __init__(self, public_key = '', secret_key = '', sync = False):
        self.time_offset = -3199
        self.b = Client(public_key, secret_key)

        if 1:
            self.time_offset = self._get_time_offset()

    def _get_time_offset(self):
        res = self.b.get_server_time()
        #print("Server time is", res['serverTime'] - int(time.time() * 1000))
        return res['serverTime'] - int(time.time() * 1000)

    def synced(self, fn_name, **args):
        args['timestamp'] = int(time.time() - self.time_offset)
        return getattr(self.b, fn_name)(**args)

"""* this creates a Client object from the Binance class with the api keys and synced to exchange
   * on top of this, i believe sync is necc to access your Binance wallet?"""
Client = Binance(public_key = bkey1['api_key'], secret_key = bkey1['api_secret'], sync=True)

"""* this gets your binance wallet amounts for the currencies to trade with, ie btc eth bnb usdt"""
def get_acct_balance(str):
    balance = Client.synced('get_asset_balance', asset=str) #returns a dict
    print(balance["asset"], ":", balance["free"])
    return (float(balance["free"]))

"""* this gets the relative prices for the coins I want to focus on. Will be expanded in the future, optimization can also 
   * be better here. Might be better to send and receive an array to this fct"""
def get_ticker_price(x):
    prices = client.get_all_tickers() #returns a list of dict's
    solo_price = prices[x] #might not need this but for simplicity i put it in, opens a spot in the string
    #print(solo_price["symbol"], ":", solo_price["price"])
    return (float(solo_price["price"]))

"""* 
   * PRE: Needs an array of 4 floats
   * POST: Will dispatch a bool T or F value
   * Purpose: This will calculate the results of possible arbitrages. """
def calc_tri_arb_btcethbnb(a):
    arb = a[0]*a[1]
    if ((arb*.94) > a[2]):
        print("Trade Profitable!")
        return (arb - a[2])
    else:
        print("Trade Not Profitable")
        return (arb - a[2])

def calc_tri_arb_btccvcbnb(a):
    arb = a[0]/a[1]
    if (arb > a[2]):
        print("Trade Profitable!")
        return (arb - a[2])
    else:
        print("Trade Not Profitable")
        return (arb - a[2])

#*************ACTUAL MAIN RUN***********
s_btc_b  = get_acct_balance("BTC")
s_eth_b  = get_acct_balance("ETH")
s_bnb_b  = get_acct_balance("BNB")
s_usdt_b = get_acct_balance("USDT")


ethbtc_tic = get_ticker_price(0)
ltcbtc_tic = get_ticker_price(1)
bnbbtc_tic = get_ticker_price(2)
bnbeth_tic = get_ticker_price(10)
btcusdt_tic = get_ticker_price(11)
ethusdt_tic = get_ticker_price(12)
cvcbtc_tic = get_ticker_price(326)
cvcbnb_tic = get_ticker_price(328)
a_opp_1 = [ethbtc_tic, bnbeth_tic, bnbbtc_tic] #first possible arb combo to try
a_opp_2 = [cvcbtc_tic, cvcbnb_tic, bnbbtc_tic]
#a_opp_3 = [s_btc_b, ]
#a_opp_4 = [s_btc_b, ]
#a_opp_5 = [s_btc_b, ]

p = calc_tri_arb_btcethbnb(a_opp_1)
z = calc_tri_arb_btccvcbnb(a_opp_2)
print(p)
print(z)
#calc_tri_arb(a_opp_2)
#calc_tri_arb(a_opp_3)
#calc_tri_arb(a_opp_4)
#calc_tri_arb(a_opp_5)


#########Experimental Branch*****************
#etcbtc_tic = get_ticker_price(59)
