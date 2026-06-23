class Product:

    def __init__(
        self,
        name,
        stock
    ):
        self.name = name
        self.stock = stock


class Perishable(Product):
    pass


class Electronics(Product):
    pass


inventory = {
    "Milk": 5,
    "Laptop": 20,
    "Bread": 3
}

low_stock = {
    item
    for item, qty
    in inventory.items()
    if qty < 10
}

print("Inventory")

for item, qty in inventory.items():
    print(item, qty)

print(
    "Low Stock Items:",
    low_stock
)

