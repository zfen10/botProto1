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

#this is how you get all account balances
##pprint is how to print out dict's really easily
#pprint.pprint(client_info)

#dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
#print ("name: ", dict['Name'])
#print ("age: ", dict['Age'])

#quantity = [0.001, 0.002, 0.003, 0.005, 0.01, 0.015, 0.03]  # Limit Amounts For Trading
#print(quantity[0])

#to print shit out from a dictionary, do this
#balance = Client.synced('get_asset_balance', asset=str)
#print(balance["asset"], ":", balance["free"])

# the following is triangular arbitrage put into code :)

def doArb(a):
    #arb1 = a[0]/a[1]
    #arb2 = arb1/a[2]
    #endAmount = arb2*a[3]
    #return endAmount
    arb = a[1]/a[2]
    if(arb>a[3]):
        print("Trade Profitable!")
        return(arb-a[3])
    else:
        print("Trade Not Profitable")
        return (arb - a[3])

def doArb1(a):
    #arb1 = a[0]/a[1]
    #arb2 = arb1/a[2]
    #endAmount = arb2*a[3]
    #return endAmount
    arb = a[1]*a[2]
    if(arb>a[3]):
        print("Trade Profitable!")
        return(arb-a[3])
    else:
        print("Trade Not Profitable")
        return (arb - a[3])

a = 0.00002645 #cvcbtc
b = 0.01365000 #cvcbnb
c = 0.00193110 #bnbbtc
startAmount = 0.00337718
z = [startAmount, a, b, c]
d = 0.06942600
e = 0.02780300
f =0.00193130
h = [startAmount, d, e, f]


endAmount = doArb(z)
endAmount1 = doArb1(h)

print(endAmount)
print(endAmount1)
#endAmount = 0

#arb1 = startAmount*a
#arb2 = arb1/b
#endAmount = arb2*c
#print("The starting amound is:", startAmount)
#print("The ending amount is:", endAmount)

#prices = client.get_all_tickers() #returns a list of dict's
#pprint.pprint(prices)
# Function definition is here
"""def changeme( anyList ):
   "This changes a passed list into this function"
   anyList.append([1,2,3,4]);
   print ("Values inside the function: ", anyList)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme(mylist)
theList = [11,12,13,15]
changeme(theList)
print("Values outside the function: ", mylist)
print("Vales outside the function theList: ", theList)"""