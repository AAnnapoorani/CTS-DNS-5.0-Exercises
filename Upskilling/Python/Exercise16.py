# Exercise 16

def area_of_circle(r):
	if r < 0:
		return "Invalid Radius"

	import math

	return math.pi * r * r


radius = 3

print(area_of_circle(radius))
