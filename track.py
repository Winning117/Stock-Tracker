import yfinance as yf

NORMAL = '\033[39m'
GREEN = '\033[32m'
RED = '\033[31m'

total_gains = 0


def main():
    parse_stocks_file()

    if total_gains > 0:
        print(f"Total gains: {GREEN}${format(total_gains, '.2f')}{NORMAL}")
    else:
        print(f"Total gains: {RED}${format(total_gains, '.2f')}{NORMAL}")


def parse_stocks_file():
    with open('my_stocks.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace(" ", "").replace("\n", "").split(",")
            print_price(line)


def print_price(line):
    try:
        stock_name = line[0]
        purchase_price = float(line[1])
        num_shares = float(line[2])
        current_price = yf.Ticker(stock_name).info['regularMarketPrice']
        gain = current_price - purchase_price
        total_gain = gain*num_shares

        print(f"Stock: {stock_name}")
        if gain > 0:
            print(f"Gain per share: {GREEN}${format(gain, '.2f')}{NORMAL}")
        else:
            print(f"Gain per share: {RED}${format(gain, '.2f')}{NORMAL}")

        if total_gain > 0:
            print(f"Total gain for this stock: {GREEN}${format(total_gain, '.2f')}{NORMAL}")
        else:
            print(f"Total gain for this stock: {RED}${format(total_gain, '.2f')}{NORMAL}")

        global total_gains
        total_gains += total_gain

        print()
    except KeyError:
        print(f"ERROR: Unable to find a stock with the name {stock_name}!")


if __name__ == "__main__":
    main()
