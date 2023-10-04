class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(" ".join(f"{h:>10}" for h in headers))
        print((("-" * 10) + " ") * len(headers))

    def row(self, rowdata):
        print(" ".join(f"{d:>10}" for d in rowdata))


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
    formatter = TextTableFormatter()
    print_table(portfolio, ["name", "shares", "price"], formatter)
