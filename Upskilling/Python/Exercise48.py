# Exercise 48

class CartItem:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def subtotal(self):
        return self.price * self.quantity


class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        self.items = [
            item for item in self.items
            if item.name != name
        ]

    def calculate_total(self):
        return sum(item.subtotal() for item in self.items)

    def print_receipt(self):

        print("----- RECEIPT -----")

        for item in self.items:
            print(
                item.name,
                item.quantity,
                item.subtotal()
            )

        total = self.calculate_total()

        gst = total * 0.18

        final_total = total + gst

        print("Subtotal =", total)
        print("GST =", gst)
        print("Final Total =", final_total)


cart = ShoppingCart()

cart.add_item(CartItem("Laptop", 50000, 1))
cart.add_item(CartItem("Mouse", 500, 2))

cart.print_receipt()

