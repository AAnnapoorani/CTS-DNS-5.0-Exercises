# Exercise 32

def add_expense(expenses, amount):

	if amount <= 0:
		return "Invalid Expense Amount"

	expenses.append(amount)

	return expenses


expenses = [1000, 1500, 2000]

print(add_expense(expenses, 500))
