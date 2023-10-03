def print_table(objects, headers):
    """Make a nicely formatted table from arbitrary data."""
    for header in headers:
        print(f"{header:>10}", end=" ")
    print()
    print((("-" * 10) + " ") * len(headers))
    for object in objects:
        for header in headers:
            print(f"{getattr(object, header):>10}", end=" ")
        print()


if __name__ == "__main__":
    import stock

    portfolio = stock.read_portfolio("Data/portfolio.csv")
    print_table(portfolio, ["name", "shares", "price"])
    print()
    print_table(portfolio, ["shares", "name"])
