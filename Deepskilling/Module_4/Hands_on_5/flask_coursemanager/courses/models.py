from courses import db

class Department(db.Model):
    __tablename__ = "departments"
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(100),
        nullable=False
    )
    head_of_dept = db.Column(
        db.String(100)
    )
    budget = db.Column(
        db.Numeric(10, 2)
    )
    courses = db.relationship(
        "Course",
        backref="department",
        lazy=True
    )
    students = db.relationship(
        "Student",
        backref="department",
        lazy=True
    )


class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    code = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    credits = db.Column(
        db.Integer,
        nullable=False
    )

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id")
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "credits": self.credits,
            "department_id": self.department_id
        }


class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    first_name = db.Column(
        db.String(50)
    )

    last_name = db.Column(
        db.String(50)
    )

    email = db.Column(
        db.String(100),
        unique=True
    )

    enrollment_year = db.Column(
        db.Integer
    )

    department_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "departments.id"
        )
    )

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "enrollment_year": self.enrollment_year,
            "department_id": self.department_id
        }


class Enrollment(db.Model):

    __tablename__ = "enrollments"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "students.id"
        )
    )

    course_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "courses.id"
        )
    )

    grade = db.Column(
        db.String(5)
    )