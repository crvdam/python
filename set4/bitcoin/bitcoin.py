import sys
import requests
import json

try:
    n = float(sys.argv[1])
except:
    sys.exit("Missing command-line argument")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

o = response.json()
result = float(o["bpi"]["USD"]["rate_float"]) * n
print(f"${result:,.4f}")
