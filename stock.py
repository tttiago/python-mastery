from structure import Structure
from validate import PositiveFloat, PositiveInteger, String


class Stock(Structure):
    _fields = ("name", "shares", "price")
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
