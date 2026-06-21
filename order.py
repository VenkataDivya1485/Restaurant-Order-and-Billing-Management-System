class Order:
    """This class manages customer orders"""

    def __init__(self):
        self.order_items = []

    def add_item(self, item):
        """Add an item to the order"""
        self.order_items.insert(len(self.order_items), item)
        print(item.name, "added to order.")

    def remove_item(self, item_id):
        """Remove an item from the order using item ID"""
        for item in self.order_items:
            if item.item_id == item_id:
                self.order_items.remove(item)
                print("Item removed from order.")
                return
        print("Item not found in order.")

    def view_order(self):
        """Display all ordered items"""
        if len(self.order_items) == 0:
            print("Order is empty.")
        else:
            print("\n----- ORDER DETAILS -----")
            for item in self.order_items:
                print(item)

    def calculate_total(self):
        """Calculate total bill amount"""
        total = 0
        for item in self.order_items:
            total += item.price
        return total
