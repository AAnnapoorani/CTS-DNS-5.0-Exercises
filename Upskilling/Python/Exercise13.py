# Exercise 13

def even_or_odd(num):
	if not isinstance(num, int):
		return "Invalid Input"

	if num % 2 == 0:
		return "Even"
	else:
		return "Odd"


num = 8

print(even_or_odd(num))
