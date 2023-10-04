class Stock:
    __slots__ = ("name", "_shares", "_price")
    _types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"{type(self).__name__}({self.name!r}, {self.shares!r}, {self.price!r})"

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f"Expected a {self._types[1].__name__}")
        if value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f"Expected a {self._types[2].__name__}")
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


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
