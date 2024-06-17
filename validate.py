from inspect import signature


class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)


class Typed(Validator):
    expected_type = object

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f"Expected {cls.expected_type}")
        return super().check(value)


class Integer(Typed):
    expected_type = int


class Float(Typed):
    expected_type = float


class String(Typed):
    expected_type = str


class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError("Expected >= 0")
        return super().check(value)


class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError("Must be non-empty")
        return super().check(value)


class PositiveInteger(Integer, Positive):
    pass


class PositiveFloat(Float, Positive):
    pass


class NonEmptyString(String, NonEmpty):
    pass


def validated(func):
    sig = signature(func)
    annotations = dict(func.__annotations__)
    retcheck = annotations.pop("return", None)

    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        errors = []
        for name, validator in annotations.items():
            try:
                validator.check(bound.arguments[name])
            except Exception as e:
                errors.append(f"    {name}: {e}")

        if errors:
            raise TypeError("Bad Arguments\n" + "\n".join(errors))

        result = func(*args, **kwargs)

        if retcheck:
            try:
                retcheck.check(result)
            except Exception as e:
                raise TypeError(f"Bad Return Value: {e}") from None

        return result

    return wrapper


if __name__ == "__main__":

    class Stock:
        name = String()
        shares = PositiveInteger()
        price = PositiveFloat()

        _types = (str, int, float)

        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

        def __repr__(self):
            return f"{type(self).__name__}({self.name!r}, {self.shares!r}, {self.price!r})"

        def __eq__(self, other):
            return isinstance(other, Stock) and (
                (self.name, self.shares, self.price) == (other.name, other.shares, other.price)
            )

        @classmethod
        def from_row(cls, row):
            values = [func(val) for func, val in zip(cls._types, row)]
            return cls(*values)

        @property
        def cost(self):
            return self.shares * self.price

        def sell(self, nshares):
            self.shares -= nshares
