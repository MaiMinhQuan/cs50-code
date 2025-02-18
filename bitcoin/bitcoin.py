import sys
import json
import requests

if len(sys.argv) == 2:
    try:
        x = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = response.json()
    rate = response["bpi"]["USD"]["rate_float"]
    print(f"${x*rate:,.4f}")
except requests.RequestException:
    print("RequestException")