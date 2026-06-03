# Exercise 10

def next_year_age():
	age = input("Enter your age: ")

	if not age.isdigit():
		print("Invalid Age")
		return

	age = int(age)

	print(f"Next year you'll be {age + 1}")


next_year_age()
