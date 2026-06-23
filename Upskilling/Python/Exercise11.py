# Exercise 11

def kg_to_pounds():
	try:
		kg = float(input("Enter weight in kilograms: "))

		if kg <= 0:
			print("Weight must be positive")
			return

		lbs = kg * 2.20462

		print(f"Weight in Pounds: {lbs:.2f}")

	except ValueError:
		print("Invalid input")


kg_to_pounds()

