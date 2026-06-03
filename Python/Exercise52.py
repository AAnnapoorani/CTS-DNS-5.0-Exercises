import json

students = {}


def add_grade(student, grade):

    if not (0 <= grade <= 100):
        print("Invalid Grade")
        return

    students.setdefault(
        student,
        []
    ).append(grade)


def calculate_gpa(student):

    grades = students.get(student)

    if not grades:
        return 0

    return sum(grades) / len(grades)


def save_data():

    with open(
        "grades.json",
        "w"
    ) as file:
        json.dump(
            students,
            file,
            indent=4
        )


add_grade("Madhi", 85)
add_grade("Madhi", 95)

print(
    "GPA:",
    calculate_gpa("Madhi")
)

save_data()

