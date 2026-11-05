import sys
import time

# Parent Class
class Product:
    """
    Represents a generic item in the store.
    """
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_price(self, quantity):
        """
        Polymorphism: This method acts as the blueprint.
        """
        return self.price * quantity

    def display_info(self):
        return f"[{self.product_id}] {self.name}: ${self.price:.2f}"

# Child Class 1: Physical Product
class PhysicalProduct(Product):
    """
    Inherits from Product. Adds shipping logic.
    """
    def __init__(self, product_id, name, price, weight_kg, shipping_cost):
        super().__init__(product_id, name, price)
        self.weight_kg = weight_kg
        self.shipping_cost = shipping_cost

    def get_price(self, quantity):
        """
        Polymorphism: Overrides parent to add shipping costs.
        """
        base_cost = super().get_price(quantity)
        return base_cost + (self.shipping_cost * quantity)

    def display_info(self):
        return f"{super().display_info()} (+ ${self.shipping_cost:.2f} shipping)"

# Child Class 2: Digital Product
class DigitalProduct(Product):
    """
    Inherits from Product. Adds discount logic.
    """
    def __init__(self, product_id, name, price, file_size_mb):
        super().__init__(product_id, name, price)
        self.file_size_mb = file_size_mb

    def get_price(self, quantity):
        """
        Polymorphism: Overrides parent to add bulk discount (10% off for 5+ items).
        """
        total = super().get_price(quantity)
        if quantity >= 5:
            discount = total * 0.10
            return total - discount
        return total

    def display_info(self):
        return f"{super().display_info()} (Instant Download)"

# Application Logic
class StoreApp:
    def __init__(self):
        # Dictionary for inventory
        self.inventory = {
            "101": PhysicalProduct("101", "Gaming Laptop", 1200.00, 2.5, 25.00),
            "102": PhysicalProduct("102", "Mechanical Keyboard", 85.50, 1.2, 10.00),
            "201": DigitalProduct("201", "Antivirus License", 45.00, 150),
            "202": DigitalProduct("202", "E-Book: Python Mastery", 15.00, 5)
        }
        # List for cart
        self.cart = []

    def show_catalog(self):
        print("\n--- Product Catalog ---")
        for pid, product in self.inventory.items():
            print(product.display_info())

    def add_to_cart(self):
        try:
            p_id = input("\nEnter Product ID to buy: ")
            if p_id not in self.inventory:
                print("Error: Product ID not found.")
                return
            
            qty = int(input("Enter quantity: "))
            if qty <= 0:
                print("Error: Quantity must be positive.")
                return
            
            selected_product = self.inventory[p_id]
            self.cart.append((selected_product, qty))
            print(f"Added {qty} x {selected_product.name} to cart.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    def checkout(self):
        print("\n--- Checkout Summary ---")
        
        if not self.cart:
            print("Your cart is empty.")
            time.sleep(1.5)
            return

        total_cost = 0.0
        
        for item, qty in self.cart:
            cost = item.get_price(qty)
            total_cost += cost
            print(f"- {item.name} (x{qty}): ${cost:.2f}")

        print("------------------------")
        print(f"Grand Total: ${total_cost:.2f}")
        
        # Simulate payment process
        print("\nProcessing payment...")
        time.sleep(1.5) 
        print("Payment Successful! Thank you for shopping.")
        
        # Clear cart for the next user instead of exiting
        self.cart.clear()
        
        # Short pause before showing menu again
        time.sleep(1.5)

    def run(self):
        print("Welcome to the Python Store!")
        while True:
            print("\n1. View Catalog")
            print("2. Add Item")
            print("3. Checkout")
            print("4. Exit")
            choice = input("Select: ")
            
            if choice == '1': self.show_catalog()
            elif choice == '2': self.add_to_cart()
            elif choice == '3': self.checkout()
            elif choice == '4': break

# This guard block ensures the game doesn't run when imported by the test file
if __name__ == "__main__":
    app = StoreApp()
    app.run()
