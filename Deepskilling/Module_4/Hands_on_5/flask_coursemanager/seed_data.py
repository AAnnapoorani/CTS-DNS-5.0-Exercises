from app import app
from courses import db
from courses.models import Student, Enrollment

with app.app_context():

    student = Student(
        first_name="Anu",
        last_name="Raj",
        email="anu@gmail.com",
        enrollment_year=2024,
        department_id=1
    )

    db.session.add(student)
    db.session.commit()

    enrollment = Enrollment(
        student_id=student.id,
        course_id=1,
        grade="A"
    )

    db.session.add(enrollment)
    db.session.commit()

    print("Data inserted")