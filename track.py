import yfinance as yf
from coinmarketcap import Market

NORMAL = '\033[39m'
GREEN = '\033[32m'
RED = '\033[31m'

overall_gains = 0
total_spent = 0


def main():
    parse_crypto_file()
    parse_stocks_file()

    print(f"Total spent: ${total_spent}")
    print_colored_price("OVERALL GAINS:", overall_gains)


def parse_stocks_file():
    with open('my_stocks.txt') as f:
        lines = f.readlines()
        for line in lines:
            if "#" in line:  # ignore comments
                continue
            elif line.count(',') is not 2:  # ensure there are only 2 commas in the line
                line = line.strip('\n')
                print(f"ERROR: There are more than 2 commas in the line [{RED}{line}{NORMAL}]\n")
                continue
            else:
                line = line.replace(" ", "").replace("\n", "").split(",")
                parse_stock(line)


def parse_crypto_file():
    with open('my_crypto.txt') as f:
        lines = f.readlines()
        for line in lines:
            if "#" in line:  # ignore comments
                continue
            elif line.count(',') is not 2:  # ensure there are only 2 commas in the line
                line = line.strip('\n')
                print(f"ERROR: There are more than 2 commas in the line [{RED}{line}{NORMAL}]\n")
                continue
            else:
                line = line.replace(" ", "").replace("\n", "").split(",")
                crypto_name = line[0]
                purchase_price_per_share = float(line[1])
                num_shares = float(line[2])
                current_price = get_current_crypto_price(crypto_name)
                gain = current_price - purchase_price_per_share
                total_gain = gain*num_shares

                global overall_gains
                overall_gains += total_gain

                global total_spent
                total_spent += purchase_price_per_share*num_shares

                print(f"Cryptocurrency: {crypto_name}")
                print(f"Number of shares: {num_shares}")
                print(f"Purchase price per share: ${format(purchase_price_per_share, '.2f')}")
                print(f"Current price per share: ${format(current_price, '.2f')}")
                print_colored_price("Gain per share:", gain)
                print_colored_price("Total gain for this cryptocurrency:", total_gain)
                print()


def print_colored_price(message, value):
    """
    Prints the gains/losses in colored format
    """
    number = "{0:,.2f}".format(value)
    if value >= 0:
        print(f"{message} {GREEN}${number}{NORMAL}")
    else:
        print(f"{message} {RED}${number}{NORMAL}")


def parse_stock(line):
    try:
        stock_name = line[0]
        purchase_price_per_share = float(line[1])
        num_shares = float(line[2])
        current_price = yf.Ticker(stock_name).info['regularMarketPrice']
        gain = current_price - purchase_price_per_share
        total_gain = gain*num_shares

        print(f"Stock: {stock_name}")
        print(f"Number of shares: {num_shares}")
        print(f"Purchase price per share: ${format(purchase_price_per_share, '.2f')}")
        print(f"Current price per share: ${format(current_price, '.2f')}")
        print_colored_price("Gain per share:", gain)
        print_colored_price("Total gain for this stock:", total_gain)
        print()

        global overall_gains
        overall_gains += total_gain

        global total_spent
        total_spent += purchase_price_per_share*num_shares
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
