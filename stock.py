import csv


class Stock:
    _types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares


def print_portfolio(portfolio):
    """Make a nicely formatted table showing stock data."""
    print(f"{'name':>10} {'shares':>10} {'price':>10}")
    print((("-" * 10) + " ") * 3)
    for s in portfolio:
        print(f"{s.name:>10} {s.shares:10} {s.price:10.2f}")


if __name__ == "__main__":
    from reader import read_csv_as_instances

    portfolio = read_csv_as_instances("Data/portfolio.csv", Stock)
    print_portfolio(portfolio)
