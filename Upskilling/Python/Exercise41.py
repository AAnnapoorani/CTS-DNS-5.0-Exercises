import json

class Employee:

	def __init__(self, emp_id, name, salary):
		self.emp_id = emp_id
		self.name = name
		self.salary = salary

	def __str__(self):
		return f"ID:{self.emp_id}, Name:{self.name}, Salary:{self.salary}"


employees = {
	1: Employee(1, "Madhi", 50000),
	2: Employee(2, "John", 60000)
}


def save_employees():
	data = {}

	for emp_id, emp in employees.items():
		data[emp_id] = {
			"name": emp.name,
			"salary": emp.salary
		}

	with open("emps.json", "w") as file:
		json.dump(data, file, indent=4)


def load_employees():
	with open("emps.json", "r") as file:
		return json.load(file)


save_employees()

loaded = load_employees()

for emp_id, details in loaded.items():
	print(emp_id, details)


