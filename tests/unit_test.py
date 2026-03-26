import unittest
# PRO TIP: Import the classes instead of copying them. 
# This guarantees you are testing the ACTUAL code.
from source_code import Product, PhysicalProduct, DigitalProduct 

class TestShop(unittest.TestCase):
    def setUp(self):
        # Create dummy data for testing
        self.laptop = PhysicalProduct("101", "Laptop", 1000.00, 2.0, 50.00)
        self.ebook = DigitalProduct("201", "E-Book", 20.00, 10)

    def test_shipping(self):
        """Test that shipping is added correctly for Physical Products"""
        # (1000 * 2) + (50 * 2) = 2100
        self.assertEqual(self.laptop.get_price(2), 2100.00)

    def test_discount(self):
        """Test that 10% discount is applied for 5+ Digital Products"""
        # (20 * 5) - 10% = 90
        self.assertEqual(self.ebook.get_price(5), 90.00)

if __name__ == '__main__':
    unittest.main()
