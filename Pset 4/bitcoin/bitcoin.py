import requests
import sys
import json

if len(sys.argv) == 2:
    if float(sys.argv[1]):
        try:
            response = requests.get(
                "https://api.coindesk.com/v1/bpi/currentprice.json"
            )

            data = response.json()

            rate = data["bpi"]["USD"]["rate_float"]

            price = float(rate) * float(sys.argv[1])

            print(f"${price:,.4f}")

        except requests.RequestException:
            pass

    else:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument ")
