import time
from decimal import Decimal, ROUND_HALF_UP

# Money uses Decimal, not float: 0.1 + 0.2 is exactly 0.3 with Decimal,
# but 0.30000000000000004 with float.
CENT = Decimal("0.01")
BULK_DISCOUNT_RATE = Decimal("0.10")
BULK_DISCOUNT_MIN_QTY = 5


def to_money(amount):
    """Rounds an amount to whole cents."""
    return Decimal(amount).quantize(CENT, rounding=ROUND_HALF_UP)


# Parent Class
class Product:
    """Represents a generic item in the store."""

    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = Decimal(price)

    def get_price(self, quantity):
        """Polymorphism: subclasses override this with their own pricing rules."""
        return to_money(self.price * quantity)

    def display_info(self):
        return f"[{self.product_id}] {self.name}: ${self.price:.2f}"


# Child Class 1: Physical Product
class PhysicalProduct(Product):
    """Inherits from Product. Adds a shipping cost per item."""

    def __init__(self, product_id, name, price, weight_kg, shipping_cost):
        super().__init__(product_id, name, price)
        self.weight_kg = Decimal(weight_kg)
        self.shipping_cost = Decimal(shipping_cost)

    def get_price(self, quantity):
        """Overrides the parent to add shipping costs."""
        return to_money(super().get_price(quantity) + self.shipping_cost * quantity)

    def display_info(self):
        return f"{super().display_info()} ({self.weight_kg} kg, + ${self.shipping_cost:.2f} shipping)"


# Child Class 2: Digital Product
class DigitalProduct(Product):
    """Inherits from Product. Adds a bulk discount."""

    def __init__(self, product_id, name, price, file_size_mb):
        super().__init__(product_id, name, price)
        self.file_size_mb = file_size_mb

    def get_price(self, quantity):
        """Overrides the parent: 10% off for 5 or more items."""
        total = super().get_price(quantity)
        if quantity >= BULK_DISCOUNT_MIN_QTY:
            total -= total * BULK_DISCOUNT_RATE
        return to_money(total)

    def display_info(self):
        return f"{super().display_info()} (Instant Download, {self.file_size_mb} MB)"


# Application Logic
class StoreApp:
    def __init__(self):
        # Dictionary for O(1) lookup by product ID
        self.inventory = {
            "101": PhysicalProduct("101", "Gaming Laptop", "1200.00", "2.5", "25.00"),
            "102": PhysicalProduct("102", "Mechanical Keyboard", "85.50", "1.2", "10.00"),
            "201": DigitalProduct("201", "Antivirus License", "45.00", 150),
            "202": DigitalProduct("202", "E-Book: Python Mastery", "15.00", 5),
        }
        self.cart = []  # list of (product, quantity)

    # --- Business logic (no input/print, so it can be unit tested) ---

    def add_item(self, product_id, quantity):
        """Adds a product to the cart. Raises ValueError for invalid input."""
        if product_id not in self.inventory:
            raise ValueError("Product ID not found.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        product = self.inventory[product_id]
        self.cart.append((product, quantity))
        return product

    def cart_total(self):
        """Total price of everything in the cart."""
        return to_money(sum((item.get_price(qty) for item, qty in self.cart), Decimal("0")))

    # --- Console interface ---

    def show_catalog(self):
        print("\n--- Product Catalog ---")
        for product in self.inventory.values():
            print(product.display_info())

    def add_to_cart(self):
        p_id = input("\nEnter Product ID to buy: ").strip()
        try:
            qty = int(input("Enter quantity: "))
            product = self.add_item(p_id, qty)
            print(f"Added {qty} x {product.name} to cart.")
        except ValueError as error:
            # int() raises ValueError for text; add_item raises it for bad IDs or quantities
            message = str(error)
            if message.startswith("invalid literal"):
                message = "Please enter a whole number for the quantity."
            print(f"Error: {message}")

    def checkout(self):
        print("\n--- Checkout Summary ---")
        if not self.cart:
            print("Your cart is empty.")
            return

        for item, qty in self.cart:
            print(f"- {item.name} (x{qty}): ${item.get_price(qty):.2f}")
        print("------------------------")
        print(f"Grand Total: ${self.cart_total():.2f}")

        print("\nProcessing payment...")
        time.sleep(1.5)  # simulated payment
        print("Payment Successful! Thank you for shopping.")
        self.cart.clear()  # ready for the next customer

    def run(self):
        print("Welcome to the Python Store!")
        actions = {"1": self.show_catalog, "2": self.add_to_cart, "3": self.checkout}
        while True:
            print("\n1. View Catalog\n2. Add Item\n3. Checkout\n4. Exit")
            choice = input("Select: ").strip()
            if choice == "4":
                break
            action = actions.get(choice)
            if action:
                action()
            else:
                print("Please choose 1, 2, 3 or 4.")


# Only start the store when run directly, not when imported by the tests
if __name__ == "__main__":
    StoreApp().run()
