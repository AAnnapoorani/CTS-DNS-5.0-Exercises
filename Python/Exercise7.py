# Exercise 7

def split_bill(total, people):
	if people <= 0:
		return "Invalid number of people"

	return total / people


print(split_bill(250.75, 3))
