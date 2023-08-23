import sys
import json
inport request

if len(sys.argv) == 2:
    try:
        x = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")

try:
    response = request.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = response.json()