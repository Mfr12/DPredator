import json
from pprint import pprint
import os

import urllib.request
urllib.request.urlretrieve('https://api.coinmarketcap.com/v1/ticker/', 'data.json')

data = json.load(open('data.json',"rb"))

a = data[0]["price_usd"].replace("'","")
b = data[1]["price_usd"].replace("'","")
c = data[2]["price_usd"].replace("'","")
d = data[3]["price_usd"].replace("'","")
e = data[4]["price_usd"].replace("'","")

print("{Crypto Currency}\n")
print("Bitcoin -> " + a)
print("Etheruem -> " + b)
print("Ripple -> " + c)
print("Bitcoin Cash -> " + d)
print("Litecoin -> " + e)

wait = input("\nPress [Enter] to go back...")
os.system("rm data.json")
os.system("python3 DPredator.py")
