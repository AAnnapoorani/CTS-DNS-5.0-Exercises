
# Exercise 35

def display_coordinates(coords):

	if len(coords) != 2:
		return "Invalid Coordinates"

	x, y = coords

	print(f"X Coordinate: {x}")
	print(f"Y Coordinate: {y}")


coordinates = (15, 30)

display_coordinates(coordinates)

