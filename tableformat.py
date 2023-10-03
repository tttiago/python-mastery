def print_table(records, headers):
    """Make a nicely formatted table from arbitrary data."""
    print(" ".join(f"{header:>10}" for header in headers))
    print((("-" * 10) + " ") * len(headers))
    for record in records:
        print(" ".join(f"{getattr(record, header):>10}" for header in headers))


if __name__ == "__main__":
    import stock

    portfolio = stock.read_portfolio("Data/portfolio.csv")
    print_table(portfolio, ["name", "shares", "price"])
    print()
    print_table(portfolio, ["shares", "name"])
