import csv


def read_csv_as_dicts(filename, types):
    """
    Read CSV data into a list of dictionaries with optional type conversion.
    """
    with open(filename) as file:
        return csv_as_dicts(file, types)


def read_csv_as_instances(filename, cls):
    """
    Read CSV data into a list of instances.
    """
    with open(filename) as file:
        return csv_as_instances(file, cls)


def csv_as_dicts(lines, types):
    """
    Transform CSV lines into a list of dictionaries with optional type conversion.
    """
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = {name: func(val) for name, func, val in zip(headers, types, row)}
        records.append(record)
    return records


def csv_as_instances(lines, cls):
    """
    Transform CSV lines into a list of instances.
    """
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records
