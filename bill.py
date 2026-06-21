from order import Order

class Bill:
    def __init__(self, order):
        self.order = order

    def calculate_tax(self):
        return self.order.calculate_total() * 0.05

    def apply_discount(self):
        subtotal = self.order.calculate_total()

        if subtotal > 500:
            return subtotal * 0.10
        return 0

    def calculate_final_amount(self):
        subtotal = self.order.calculate_total()
        tax = self.calculate_tax()
        discount = self.apply_discount()

        return subtotal + tax - discount

    def display_bill(self):
        print("\n----- BILL -----")

        for item in self.order.order_items:
            print(f"{item.name} - ₹{item.price}")

        print("----------------")
        print("Total Amount:", self.calculate_final_amount())
