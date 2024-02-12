from typing import Any


class Structure:
    _fields = ()

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f"Expected {len(self._fields)} arguments")
        for name, arg in zip(self._fields, args):
            setattr(self, name, arg)

    def __repr__(self):
        values = ", ".join(repr(getattr(self, name)) for name in self._fields)
        return f"{type(self).__name__}({values})"

    def __setattr__(self, name, value):
        if name.startswith("_") or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"No attribute {name}")
