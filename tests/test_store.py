"""Unit tests for the store. Run from the repository root with:

    python -m unittest discover tests -v
"""
import sys
import unittest
from decimal import Decimal
from pathlib import Path
from unittest.mock import patch

# Make src/ importable no matter where the tests are started from
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from store import Product, PhysicalProduct, DigitalProduct, StoreApp  # noqa: E402


class TestPricing(unittest.TestCase):
    def setUp(self):
        self.laptop = PhysicalProduct("101", "Laptop", "1000.00", "2.0", "50.00")
        self.ebook = DigitalProduct("201", "E-Book", "20.00", 10)

    def test_base_product_price(self):
        self.assertEqual(Product("1", "Pen", "1.50").get_price(3), Decimal("4.50"))

    def test_shipping_added_per_item(self):
        # (1000 * 2) + (50 * 2) = 2100
        self.assertEqual(self.laptop.get_price(2), Decimal("2100.00"))

    def test_no_discount_below_threshold(self):
        # 4 items: 20 * 4 = 80, no discount
        self.assertEqual(self.ebook.get_price(4), Decimal("80.00"))

    def test_discount_at_threshold(self):
        # 5 items: (20 * 5) - 10% = 90
        self.assertEqual(self.ebook.get_price(5), Decimal("90.00"))

    def test_no_float_rounding_errors(self):
        # 0.10 * 3 is 0.30000000000000004 with floats
        self.assertEqual(Product("2", "Sticker", "0.10").get_price(3), Decimal("0.30"))

    def test_discount_rounds_to_cents(self):
        # 3.33 * 5 = 16.65, minus 10% = 14.985 -> 14.99
        self.assertEqual(DigitalProduct("3", "App", "3.33", 1).get_price(5), Decimal("14.99"))


class TestCart(unittest.TestCase):
    def setUp(self):
        self.app = StoreApp()

    def test_empty_cart_total_is_zero(self):
        self.assertEqual(self.app.cart_total(), Decimal("0.00"))

    def test_mixed_cart_total(self):
        self.app.add_item("102", 1)  # 85.50 + 10.00 shipping = 95.50
        self.app.add_item("202", 5)  # 75.00 - 10% = 67.50
        self.assertEqual(self.app.cart_total(), Decimal("163.00"))

    def test_unknown_product_rejected(self):
        with self.assertRaises(ValueError):
            self.app.add_item("999", 1)
        self.assertEqual(self.app.cart, [])

    def test_zero_and_negative_quantity_rejected(self):
        for qty in (0, -3):
            with self.assertRaises(ValueError):
                self.app.add_item("101", qty)
        self.assertEqual(self.app.cart, [])

    def test_text_quantity_handled_without_crash(self):
        # Simulates a user typing "abc" as the quantity
        with patch("builtins.input", side_effect=["101", "abc"]), patch("builtins.print"):
            self.app.add_to_cart()
        self.assertEqual(self.app.cart, [])

    def test_checkout_clears_cart(self):
        self.app.add_item("201", 1)
        with patch("builtins.print"), patch("store.time.sleep"):
            self.app.checkout()
        self.assertEqual(self.app.cart, [])


if __name__ == "__main__":
    unittest.main()
