import sys
import requests


def main():

    # Check argv
    if len(sys.argv) == 2:

        try:
            amount_btc = float(sys.argv[1])

        except ValueError:
            print("Command-line argument is not a number")
            sys.exit(1)

    else:
        print("Missing command-line argument")

    try:
        get_request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        # Create a dictionary from the request
        r_dict = get_request.json()
        # Get the BTC price from r_dict and conver it to float
        btc_price = float(r_dict["bpi"]["USD"]["rate_float"])

        # Calculate ammount of USD dollars
        result = amount_btc * btc_price
        # Format result with 4 decimals
        print(f"${result:,.4f}")

    except requests.RequestException:
        print("Request Exception")
        sys.exit(1)


if __name__ == "__main__":
    main()
