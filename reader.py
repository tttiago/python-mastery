import csv
from typing import Any, Callable, Optional, Type


def read_csv_as_dicts(
    filename: str, types: list[Type[Callable[[str], Any]]], *, headers: Optional[list[str]] = None
) -> list[dict[str, Any]]:
    """
    Read CSV data into a list of dictionaries with optional type conversion.
    """
    with open(filename) as file:
        return csv_as_dicts(file, types, headers=headers)


def read_csv_as_instances(
    filename: str, cls: Type, *, headers: Optional[list[str]] = None
) -> list[Any]:
    """
    Read CSV data into a list of instances.
    """
    with open(filename) as file:
        return csv_as_instances(file, cls, headers=headers)


def csv_as_dicts(
    lines: Any, types: list[Type[Callable[[str], Any]]], *, headers: Optional[list[str]] = None
) -> list[dict[str, Any]]:
    """
    Transform CSV lines into a list of dictionaries with optional type conversion.
    """
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = {name: func(val) for name, func, val in zip(headers, types, row)}
        records.append(record)
    return records


def csv_as_instances(lines: Any, cls: Type, *, headers: Optional[list[str]] = None) -> list[Any]:
    """
    Transform CSV lines into a list of instances.
    """
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records
