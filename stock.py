import csv


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares


def read_portfolio(filename):
    """Read a CSV file of stock data into a list of Stocks."""
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = [Stock(row[0], int(row[1]), float(row[2])) for row in rows]
    return portfolio


def print_portfolio(portfolio):
    """Make a nicely formatted table showing stock data."""
    print(f"{'name':>10} {'shares':>10} {'price':>10}")
    print((("-" * 10) + " ") * 3)
    for s in portfolio:
        print(f"{s.name:>10} {s.shares:10} {s.price:10.2f}")


if __name__ == "__main__":
    portfolio = read_portfolio("Data/portfolio.csv")
    print_portfolio(portfolio)
