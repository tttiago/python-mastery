import csv


def read_csv_as_dicts(filename, types):
    """
    Read CSV data into a list of dictionaries with optional type conversion
    """
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = {name: func(val) for name, func, val in zip(headers, types, row)}
            records.append(record)
    return records


def read_csv_as_instances(filename, cls):
    """
    Read CSV data into a list of instances
    """
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records
