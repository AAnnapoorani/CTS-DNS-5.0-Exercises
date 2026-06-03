# Exercise 12

def check_pass(marks):
	if not (0 <= marks <= 100):
		return "Invalid Marks"

	if marks >= 40:
		return "Pass"


marks = 75

print(check_pass(marks))

