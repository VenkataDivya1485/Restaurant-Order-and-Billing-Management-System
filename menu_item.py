class MenuItem:
    """This class represents a single menu item"""

    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.item_id} - {self.name} - ₹{self.price}"

    def display_item(self):
        print(f"Item ID: {self.item_id}")
        print(f"Name: {self.name}")
        print(f"Price: ₹{self.price}")

    def update_price(self, new_price):
        self.price = new_price
        print("Price updated successfully.")

    def get_price(self):
        return self.price

    def apply_discount(self, discount_percent):
        if discount_percent < 0 or discount_percent > 100:
            print("Discount must be between 0 and 100.")
            return

        self.price = self.price - (self.price * discount_percent / 100)
        print("Discount applied successfully.")
