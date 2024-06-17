import sys

from validate import Validator


class Structure:
    _fields = ()
    _types = ()

    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop("self")
        for name, value in locs.items():
            setattr(self, name, value)

    def __repr__(self):
        values = ", ".join(repr(getattr(self, name)) for name in self._fields)
        return f"{type(self).__name__}({values})"

    def __setattr__(self, name, value):
        if name.startswith("_") or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"No attribute {name}")

    @classmethod
    def from_row(cls, row):
        rowdata = [func(val) for func, val in zip(cls._types, row)]
        return cls(*rowdata)

    @classmethod
    def create_init(cls):
        code = f"def __init__(self, {', '.join(cls._fields)}):"
        for name in cls._fields:
            code += f"\n    self.{name} = {name}"
        locs = {}
        exec(code, locs)
        cls.__init__ = locs["__init__"]

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)


def validate_attributes(cls):
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Collect all of the field names.
    cls._fields = [val.name for val in validators]

    # Collect type conversions.
    cls._types = tuple([getattr(v, "expected_type", lambda x: x) for v in validators])

    # Create the __init__ method
    if cls._fields:
        cls.create_init()

    return cls
