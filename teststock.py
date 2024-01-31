import unittest

import stock


class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock("GOOG", 100, 490.1)
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_create_keywords(self):
        s = stock.Stock(name="GOOG", shares=100, price=490.1)
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        s = stock.Stock("GOOG", 100, 490.1)
        self.assertEqual(s.cost, 49010.0)

    def test_sell(self):
        s = stock.Stock("GOOG", 100, 490.1)
        s.sell(25)
        self.assertEqual(s.shares, 75)

    def test_create_from_row(self):
        s = stock.Stock.from_row(["GOOG", 100, 490.1])
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_repr(self):
        s = stock.Stock("GOOG", 100, 490.1)
        self.assertEqual(repr(s), "Stock('GOOG', 100, 490.1)")

    def test_eq(self):
        s1 = stock.Stock("GOOG", 100, 490.1)
        s2 = stock.Stock("GOOG", 100, 490.1)
        self.assertEqual(s1, s2)


if __name__ == "__main__":
    unittest.main()
