# Exercise 34

employees = {
	"IT": {
		"John": 60000,
		"Alice": 75000
	},
	"HR": {
		"Bob": 50000
	}
}

def get_salary(department, employee):

	if department not in employees:
		return "Department Not Found"

	if employee not in employees[department]:
		return "Employee Not Found"

	return employees[department][employee]


print("Salary =", get_salary("IT", "Alice"))
