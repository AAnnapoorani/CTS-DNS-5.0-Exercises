from flask import (
    jsonify,
    request
)
from . import courses_bp

courses = []

def make_response_json(
        data,
        status_code=200):
    return jsonify({
        "success": True,
        "data": data
    }), status_code

@courses_bp.route(
    "/courses",
    methods=["GET"]
)

def get_courses():
    return make_response_json(
        courses
    )

@courses_bp.route(
    "/courses",
    methods=["POST"]
)

def create_course():
    data = request.get_json()
    required_fields = [
        "id",
        "name",
        "credits"
    ]
    for field in required_fields:
        if field not in data:
            return jsonify({
                "success": False,
                "message":
                f"{field} is required"
            }), 400
    courses.append(data)
    return make_response_json(
        data,
        201
    )

@courses_bp.route(
    "/courses/<int:course_id>",
    methods=["GET"]
)

def get_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            return make_response_json(
                course
            )
    return jsonify({
        "success": False,
        "message":
        "Course not found"
    }), 404

@courses_bp.route(
    "/courses/<int:course_id>",
    methods=["DELETE"]
)

def delete_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            courses.remove(course)
            return jsonify({
                "success": True,
                "message":
                "Course deleted successfully"
            }), 200
    return jsonify({
        "success": False,
        "message":
        "Course not found"
    }), 404