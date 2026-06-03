import statistics

def analyze_sales():

	try:
		with open("sales.txt", "r") as file:
			sales = [float(line.strip()) for line in file]

		print("Mean =", statistics.mean(sales))
		print("Median =", statistics.median(sales))

	except FileNotFoundError:
		print("Sales file not found")

	except ValueError:
		print("Invalid data found")


analyze_sales()


