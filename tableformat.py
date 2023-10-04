class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()


def print_table(records, fields, formatter):
    """Make a nicely formatted table from arbitrary data."""
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


if __name__ == "__main__":
    import reader
    import stock

    portfolio = reader.read_csv_as_instances("Data/portfolio.csv", stock.Stock)
    formatter = TableFormatter()
    print_table(portfolio, ["name", "shares", "price"], formatter)
