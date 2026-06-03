import csv
from datetime import datetime

totals = {}

current_month = datetime.now().month

with open("expenses.csv", "r") as file:

	reader = csv.DictReader(file)

	for row in reader:

		date = datetime.strptime(
			row["date"],
			"%Y-%m-%d"
		)

		if date.month == current_month:

			category = row["category"]
			amount = float(row["amount"])

			totals[category] = (
				totals.get(category, 0)
				+ amount
			)

print("Expense Summary")

for category, amount in totals.items():
	print(category, ":", amount)

