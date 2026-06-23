
# Exercise 39

class Employee:

	def work(self):
		print("Employee is working")


class Developer(Employee):

	def work(self):
		print("Developer writes code")


class Manager(Employee):

	def work(self):
		print("Manager manages team")


employees = [
	Developer(),
	Manager()
]

for emp in employees:
	emp.work()

