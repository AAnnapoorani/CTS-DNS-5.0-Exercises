from flask import Blueprint
from flask import jsonify
from flask import request

from courses import db
from courses.models import (
    Department,
    Course,
    Student,
    Enrollment
)


courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)

@courses_bp.route(
    "/departments",
    methods=["POST"]
)
def create_department():

    data = request.get_json()

    department = Department(
        name=data["name"],
        head_of_dept=data["head_of_dept"],
        budget=data["budget"]
    )

    db.session.add(department)
    db.session.commit()

    return jsonify({
        "message": "Department created successfully",
        "id": department.id
    }), 201


@courses_bp.route(
    "/departments",
    methods=["GET"]
)
def get_departments():

    departments = Department.query.all()

    result = []

    for dept in departments:

        result.append({
            "id": dept.id,
            "name": dept.name,
            "head_of_dept": dept.head_of_dept,
            "budget": str(dept.budget)
        })

    return jsonify(result)

@courses_bp.route("/courses", methods=["POST"])
def create_course():

    data = request.get_json()

    course = Course(
        name=data["name"],
        code=data["code"],
        credits=data["credits"],
        department_id=data["department_id"]
    )

    db.session.add(course)
    db.session.commit()

    return jsonify(course.to_dict()), 201

@courses_bp.route("/courses", methods=["GET"])
def get_courses():

    courses = Course.query.all()

    return jsonify([
        course.to_dict()
        for course in courses
    ])

@courses_bp.route("/courses/<int:id>", methods=["GET"])
def get_course(id):

    course = Course.query.get_or_404(id)

    return jsonify(course.to_dict())

@courses_bp.route("/courses/<int:id>", methods=["PUT"])
def update_course(id):

    course = Course.query.get_or_404(id)

    data = request.get_json()

    course.name = data["name"]
    course.code = data["code"]
    course.credits = data["credits"]

    db.session.commit()

    return jsonify(course.to_dict())

@courses_bp.route("/courses/<int:id>", methods=["DELETE"])
def delete_course(id):

    course = Course.query.get_or_404(id)

    db.session.delete(course)
    db.session.commit()

    return jsonify({
        "message": "Course deleted successfully"
    })

@courses_bp.route(
    "/courses/<int:id>/students",
    methods=["GET"]
)
def get_course_students(id):

    # Check whether course exists
    course = Course.query.get_or_404(id)

    # Find all enrollments for this course
    enrollments = Enrollment.query.filter_by(
        course_id=course.id
    ).all()

    students = []

    # Get student details for each enrollment
    for enrollment in enrollments:

        student = Student.query.get(
            enrollment.student_id
        )

        if student:
            students.append(
                student.to_dict()
            )

    return jsonify(students)
