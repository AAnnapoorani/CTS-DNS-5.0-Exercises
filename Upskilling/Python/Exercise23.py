# Exercise 23

def sum_of_digits(n):
	total = 0
	for d in str(n):
		total += int(d)
	return total

print(sum_of_digits(12345))

