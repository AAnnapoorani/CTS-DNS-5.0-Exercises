class Product:

    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price


inventory = {}

def add_product(product):
    inventory[product.product_id] = product

def update_product(product_id, quantity):
    if product_id in inventory:
        inventory[product_id].quantity = quantity

def delete_product(product_id):
    if product_id in inventory:
        del inventory[product_id]

def display():
    for p in inventory.values():
        print(p.product_id, p.name, p.quantity, p.price)


add_product(Product(101, "Laptop", 10, 50000))
add_product(Product(102, "Mouse", 50, 500))

display()

update_product(101, 20)

print("\nAfter Update")
display()

delete_product(102)

print("\nAfter Delete")
display()