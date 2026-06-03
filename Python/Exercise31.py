def display_cart(cart):
	if not cart:
		return "Cart is empty"

	print("Shopping Cart Items:")
	for item in cart:
		print(item)


cart = [100, 250, 75]

display_cart(cart)
