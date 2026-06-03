# Exercise 33

def merge_employee_data(emp1, emp2):

	if not isinstance(emp1, dict) or not isinstance(emp2, dict):
		return "Invalid Input"

	emp1.update(emp2)

	return emp1


employee1 = {
	"name": "Madhi",
	"salary": 50000
}

employee2 = {
	"department": "IT",
	"city": "Chennai"
}

print(merge_employee_data(employee1, employee2))
