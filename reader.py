import csv
from typing import Any, Callable, Optional, Type


def convert_csv(lines, conv_func, *, headers=None):
    """
    Convert CSV lines using a conversion function.
    """
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for rowno, row in enumerate(rows):
        try:
            records.append(conv_func(headers, row))
        except ValueError as e:
            print(f"Row {rowno}: Bad row: {row}")
    return records


def csv_as_dicts(
    lines: Any, types: list[Type[Callable[[str], Any]]], *, headers: Optional[list[str]] = None
) -> list[dict[str, Any]]:
    """
    Transform CSV lines into a list of dictionaries with optional type conversion.
    """
    return convert_csv(
        lines,
        lambda headers, row: {name: func(val) for name, func, val in zip(headers, types, row)},
        headers=headers,
    )


def csv_as_instances(lines: Any, cls: Type, *, headers: Optional[list[str]] = None) -> list[Any]:
    """
    Transform CSV lines into a list of instances.
    """
    return convert_csv(lines, lambda headers, row: cls.from_row(row))


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
