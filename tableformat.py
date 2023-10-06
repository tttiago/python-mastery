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


def create_formatter(name, column_formats=None, upper_headers=False):
    if name.lower() == "text":
        formatter_cls = TextTableFormatter
    elif name.lower() == "csv":
        formatter_cls = CSVTableFormatter
    elif name.lower() == "html":
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f"Unknown format {name}")

    if column_formats:

        class formatter_cls(ColumnFormatMixin, formatter_cls):
            formats = column_formats

    if upper_headers:

        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()


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

    formatter = create_formatter("csv", column_formats=["s", "d", "0.2f"], upper_headers=True)
    print_table(portfolio, ["name", "shares", "price"], formatter)

    print()
    formatter = create_formatter("text", upper_headers=True)
    print_table(portfolio, ["name", "shares", "price"], formatter)
