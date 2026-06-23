
# Exercise 40

class Employee:

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	@classmethod
	def from_string(cls, emp_string):

		name, salary = emp_string.split(",")

		return cls(name, int(salary))

	def display(self):
		print(f"Name: {self.name}")
		print(f"Salary: {self.salary}")


emp = Employee.from_string("Shubh,75000")

emp.display()

