import collections
import csv


def read_csv_as_dicts(filename, coltypes):
    """Read a CSV file as a list of dictionaries with column type conversion."""
    records = []
    with open(filename, "r") as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            record = {name: func(val) for name, func, val in zip(headings, coltypes, row)}
            records.append(record)
    return records


def read_csv_as_columns(filename, coltypes):
    """Read a CSV file as a list of dictionaries with column type conversion."""
    with open(filename, "r") as f:
        rows = csv.reader(f)
        headings = next(rows)
        records = DataCollection(headings)
        for row in rows:
            record = {name: func(val) for name, func, val in zip(headings, coltypes, row)}
            records.append(record)
    return records


class DataCollection(collections.abc.Sequence):
    def __init__(self, columns):
        # Each is a list with all the values (a column).
        self.columns = {column: [] for column in columns}

    def __len__(self):
        # All lists are assumed to have the same length.
        return len(self.columns[next(iter(self.columns))])

    def __getitem__(self, index):
        if isinstance(index, int):
            return {column: self.columns[column][index] for column in self.columns}
        elif isinstance(index, slice):
            rd = DataCollection(self.columns.keys())
            rd.columns = {column: self.columns[column][index] for column in self.columns}
            return rd
        else:
            raise TypeError("Index must be an integer or slice")

    def append(self, d):
        for k, v in d.items():
            self.columns[k].append(v)
