from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (
    Department,
    Student,
    Course,
    Enrollment,
    Professor
)

DATABASE_URL = "postgresql+psycopg2://postgres:Admin%40123@localhost:5432/college_db_orm"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

# ==================================================
# STEP 80
# Create Department
# ==================================================

cse = Department(
    dept_name="Computer Science",
    head_of_dept="Dr. Kumar",
    budget=500000
)

session.add(cse)
session.commit()

print("Department Added")

# ==================================================
# STEP 81
# Create Student
# ==================================================

student1 = Student(
    first_name="Annapoorani",
    last_name="Alagananthan",
    email="annapoorani@college.edu",
    date_of_birth=date(2004, 6, 15),
    department_id=cse.department_id,
    enrollment_year=2023
)

session.add(student1)
session.commit()

print("Student Added")

# ==================================================
# STEP 82
# Create Course
# ==================================================

course1 = Course(
    course_name="Database Systems",
    course_code="CS301",
    credits=4,
    department_id=cse.department_id
)

session.add(course1)
session.commit()

print("Course Added")

# ==================================================
# STEP 83
# Create Enrollment
# ==================================================

enrollment1 = Enrollment(
    student_id=student1.student_id,
    course_id=course1.course_id,
    enrollment_date=date.today(),
    grade="A"
)

session.add(enrollment1)
session.commit()

print("Enrollment Added")

# ==================================================
# STEP 84
# Create Professor
# ==================================================

prof1 = Professor(
    prof_name="Dr. Rajesh",
    email="rajesh@college.edu",
    department_id=cse.department_id,
    salary=85000
)

session.add(prof1)
session.commit()

print("Professor Added")

# ==================================================
# STEP 85
# Read Students
# ==================================================

print("\nStudents")

students = session.query(Student).all()

for student in students:
    print(
        student.student_id,
        student.first_name,
        student.last_name
    )

session.close()


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (
    Student,
    Course,
    Enrollment
)

DATABASE_URL = "postgresql+psycopg2://postgres:Admin%40123@localhost:5432/college_db_orm"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

# ==================================================
# STEP 86
# Query Courses
# ==================================================

print("\nCourses")

courses = session.query(Course).all()

for course in courses:
    print(
        course.course_code,
        course.course_name
    )

# ==================================================
# STEP 87
# Query Relationships
# ==================================================

print("\nStudent Enrollments")

student = session.query(Student).first()

for enrollment in student.enrollments:
    print(
        enrollment.course.course_name,
        enrollment.grade
    )

# ==================================================
# STEP 88
# Update Student
# ==================================================

student = session.query(Student).first()

student.last_name = "A"

session.commit()

print("\nStudent Updated")

# ==================================================
# STEP 89
# Delete Enrollment
# ==================================================

enrollment = session.query(Enrollment).first()

session.delete(enrollment)

session.commit()

print("Enrollment Deleted")

# ==================================================
# STEP 90
# Final Query
# ==================================================

print("\nStudents After Update")

students = session.query(Student).all()

for student in students:
    print(
        student.student_id,
        student.first_name,
        student.last_name
    )

session.close()

print("\nHands-On 6 Completed")
