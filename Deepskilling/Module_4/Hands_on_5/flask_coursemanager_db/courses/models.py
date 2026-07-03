from app import db

class Department(db.Model):
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
        db.Float
    )
    courses = db.relationship(
        'Course',
        backref='department',
        lazy=True
    )

class Course(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(100),
        nullable=False
    )
    credits = db.Column(
        db.Integer
    )
    department_id = db.Column(
        db.Integer,
        db.ForeignKey('department.id')
    )
    enrollments = db.relationship(
        'Enrollment',
        backref='course',
        lazy=True
    )

class Student(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    first_name = db.Column(
        db.String(100)
    )
    last_name = db.Column(
        db.String(100)
    )
    email = db.Column(
        db.String(120)
    )
    enrollments = db.relationship(
        'Enrollment',
        backref='student',
        lazy=True
    )

class Enrollment(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    student_id = db.Column(
        db.Integer,
        db.ForeignKey('student.id')
    )
    course_id = db.Column(
        db.Integer,
        db.ForeignKey('course.id')
    )

def __repr__(self):
    return f"<Department {self.name}>"

def __repr__(self):
    return f"<Course {self.name}>"