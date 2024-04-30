import inspect
import sys


class Structure:
    _fields = ()

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
    def set_fields(cls):
        sig = inspect.signature(cls)
        cls._fields = tuple(sig.parameters)
