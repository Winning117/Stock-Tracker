import yfinance as yf
from coinmarketcap import Market

overall_gains = 0


def main():
    parse_crypto_file()
    parse_stocks_file()

    print_colored_price("Overall gains:", overall_gains)


def parse_stocks_file():
    with open('my_stocks.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace(" ", "").replace("\n", "").split(",")
            parse_stock(line)


def parse_crypto_file():
    with open('my_crypto.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace(" ", "").replace("\n", "").split(",")
            crypto_name = line[0]
            purchase_price = float(line[1])
            num_shares = float(line[2])
            current_price = get_current_crypto_price(crypto_name)
            gain = current_price - purchase_price
            total_gain = gain*num_shares

            global overall_gains
            overall_gains += total_gain

            print(f"Cryptocurrency: {crypto_name}")
            print(f"Purchase price: ${format(purchase_price, '.2f')}")
            print(f"Current price: ${format(current_price, '.2f')}")
            print_colored_price("Gain per share:", gain)
            print_colored_price("Total gain for this cryptocurrency:", total_gain)
            print()


def print_colored_price(message, value):
    """
    Prints the gains/losses in colored format
    """
    NORMAL = '\033[39m'
    GREEN = '\033[32m'
    RED = '\033[31m'

    number = "{0:,.2f}".format(value)
    if value >= 0:
        print(f"{message} {GREEN}${number}{NORMAL}")
    else:
        print(f"{message} {RED}${number}{NORMAL}")


def parse_stock(line):
    try:
        stock_name = line[0]
        purchase_price = float(line[1])
        num_shares = float(line[2])
        current_price = yf.Ticker(stock_name).info['regularMarketPrice']
        gain = current_price - purchase_price
        total_gain = gain*num_shares

        print(f"Stock: {stock_name}")
        print(f"Purchase price: ${format(purchase_price, '.2f')}")
        print(f"Current price: ${format(current_price, '.2f')}")
        print_colored_price("Gain per share:", gain)
        print_colored_price("Total gain for this stock:", total_gain)
        print()

        global overall_gains
        overall_gains += total_gain
    except KeyError:
        print(f"ERROR: Unable to find a stock with the name {stock_name}!")


def get_current_crypto_price(crypto_name):
    coinmarketcap = Market()
    data = coinmarketcap.ticker()["data"]
    for chunk in data:
        name = data[chunk]["symbol"]
        price = data[chunk]["quotes"]["USD"]["price"]
        if name == crypto_name:
            return price


if __name__ == "__main__":
    main()
