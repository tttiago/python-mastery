from abc import ABC, abstractmethod


class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()

    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(" ".join(f"{h:>10}" for h in headers))
        print((("-" * 10) + " ") * len(headers))

    def row(self, rowdata):
        print(" ".join(f"{d:>10}" for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(str(d) for d in rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr> <th>" + "</th> <th>".join(headers) + "</th> </tr>")

    def row(self, rowdata):
        print("<tr> <td>" + "</td> <td>".join(str(d) for d in rowdata) + "</td> </tr>")


class ColumnFormatMixin:
    formats = []

    def row(self, rowdata):
        rowdata = [f"{d:{fmt}}" for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)


class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])


def create_formatter(name):
    if name.lower() == "text":
        return TextTableFormatter()
    elif name.lower() == "csv":
        return CSVTableFormatter()
    elif name.lower() == "html":
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f"Unknown format {name}")


def print_table(records, fields, formatter):
    """Make a nicely formatted table from arbitrary data."""
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")

    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


if __name__ == "__main__":
    import reader
    import stock

    portfolio = reader.read_csv_as_instances("Data/portfolio.csv", stock.Stock)

    class PortfolioFormatter(UpperHeadersMixin, TextTableFormatter):
        pass

    formatter = PortfolioFormatter()
    print_table(portfolio, ["name", "shares", "price"], formatter)
