import collections
import csv
import typing
from collections import namedtuple


def read_rides_as_tuples(filename):
    """
    Read the bus ride data as a list of tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_dictionaries(filename):
    """
    Read the bus ride data as a list of tuples
    """
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {"route": route, "date": date, "daytype": daytype, "rides": rides}
            records.append(record)
    return records


def read_rides_as_class_instances(filename):
    """
    Read the bus ride data as a list of class instances
    """

    class Row:
        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_slots_class_instances(filename):
    """
    Read the bus ride data as a list of class instances with slots
    """

    class Row:
        __slots__ = ["route", "date", "daytype", "rides"]

        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_named_tuples(filename):
    """
    Read the bus ride data as a list of named tuples
    """

    class Row(typing.NamedTuple):
        route: str
        date: str
        daytipe: str
        rides: int

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_named_tuples_older(filename):
    """
    Read the bus ride data as a list of named tuples (older code)
    """
    Row = namedtuple("Row", ["route", "date", "daytype", "rides"])
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_columns(filename):
    """
    Read the bus ride data into 4 lists, representing columns
    """
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)


class RideData(collections.abc.Sequence):
    def __init__(self):
        # Each is a list with all the values (a column).
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists are assumed to have the same length.
        return len(self.routes)

    def __getitem__(self, index):
        if isinstance(index, int):
            return {
                "route": self.routes[index],
                "date": self.dates[index],
                "daytype": self.daytypes[index],
                "rides": self.numrides[index],
            }
        elif isinstance(index, slice):
            rd = RideData()
            rd.routes = self.routes[index]
            rd.dates = self.dates[index]
            rd.daytypes = self.daytypes[index]
            rd.numrides = self.numrides[index]
            return rd
        else:
            raise TypeError("Index must be an integer or slice")

    def append(self, d):
        self.routes.append(d["route"])
        self.dates.append(d["date"])
        self.daytypes.append(d["daytype"])
        self.numrides.append(d["rides"])


if __name__ == "__main__":
    import tracemalloc

    for func in (
        read_rides_as_tuples,
        read_rides_as_dictionaries,
        read_rides_as_class_instances,
        read_rides_as_named_tuples,
        read_rides_as_named_tuples_older,
        read_rides_as_slots_class_instances,
    ):
        tracemalloc.start()
        rows = func("Data/ctabus.csv")
        current, peak = tracemalloc.get_traced_memory()
        print(
            f'{"_".join(func.__name__.split("_")[3:]):23}'
            + "Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory()
        )
        tracemalloc.stop()
