
# Exercise 37

class Employee:

	def __init__(self, name):
		self.name = name

	def display(self):
		print("Employee Name:", self.name)


emp1 = Employee("Madhi")
emp2 = Employee("John")
emp3 = Employee("Alice")

emp1.display()
emp2.display()
emp3.display()

