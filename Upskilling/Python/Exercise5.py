# Exercise 5

def distance(x1, y1, x2, y2):
	import math

	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


print(distance(0, 0, 3, 4))
# Exercise 5

def display_coordinates(coords):
	if len(coords) != 2:
		return "Invalid Coordinates"

	x, y = coords
	return f"X = {x}, Y = {y}"


coordinates = (15, 25)

print(display_coordinates(coordinates))
