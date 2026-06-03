
# Exercise 38

class Employee:

	def __init__(self, name):
		self.name = name
		self.salary = 0

	def set_salary(self, salary):
		self.salary = salary
		return self

	def apply_raise(self, percent):
		self.salary += self.salary * percent / 100
		return self

	def display(self):
		print(f"{self.name} Salary = {self.salary}")
		return self


emp = Employee("Madhi")

emp.set_salary(50000).apply_raise(10).display()

