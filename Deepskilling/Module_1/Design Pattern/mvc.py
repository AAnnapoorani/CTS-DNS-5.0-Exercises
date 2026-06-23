class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

class StudentView:
    def display_student(self, student):
        print("Student ID :", student.student_id)
        print("Name :", student.name)
        print("Grade :", student.grade)

class StudentController:
    def __init__(self, student, view):
        self.student = student
        self.view = view
    def update_name(self, new_name):
        self.student.name = new_name
    def show_details(self):
        self.view.display_student(self.student)


student = Student(101, "Madhi", "A")
view = StudentView()
controller = StudentController(student, view)
controller.show_details()
print("\nAfter Updating Name\n")
controller.update_name("Annapoorani")
controller.show_details()