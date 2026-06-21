from menu import Menu
from menu_item import MenuItem
from order import Order
from bill import Bill

class Restaurant:
    """This class controls the restaurant system"""

    def __init__(self):
        self.menu = Menu()
        self.order = Order()

    def load_menu(self):
        self.menu.add_item(MenuItem(1, "Burger", 120))
        self.menu.add_item(MenuItem(2, "Pizza", 250))
        self.menu.add_item(MenuItem(3, "Pasta", 180))
        self.menu.add_item(MenuItem(4, "Coffee", 80))

    def show_menu(self):
        self.menu.display_menu()

    def take_order(self):
        item_id = int(input("Enter item ID to order: "))

        item = self.menu.search_item(item_id)

        if item:
            self.order.add_item(item)
        else:
            print("Item not found in menu.")

    def generate_customer_bill(self):
        bill = Bill(self.order)
        bill.display_bill()
