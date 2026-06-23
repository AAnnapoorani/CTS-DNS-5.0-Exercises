employees = []

employees.append(["101", "Madhi", "Developer", 50000])
employees.append(["102", "Priya", "Tester", 40000])

print("Employee Records")

for emp in employees:
    print(emp)

search_id = "101"

for emp in employees:

    if emp[0] == search_id:
        print("\nEmployee Found")
        print(emp)

employees.remove(employees[0])

print("\nAfter Deletion")

for emp in employees:
    print(emp)