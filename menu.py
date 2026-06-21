from menu_item import MenuItem

class Menu:
    """This class manages all menu items"""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add a menu item"""
        self.items.insert(len(self.items), item)
        print(f"{item.name} added to menu.")

    def remove_item(self, item_id):
        """Remove a menu item using item ID"""
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                print("Item removed successfully.")
                return
        print("Item not found.")

    def search_item(self, item_id):
        """Search for a menu item by ID"""
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    def display_menu(self):
        """Display all menu items"""
        if not self.items:
            print("Menu is empty.")
        else:
            print("\n----- MENU -----")
            for item in self.items:
                print(item)
