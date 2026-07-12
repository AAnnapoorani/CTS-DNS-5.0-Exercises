from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "Annapoorani"
    }
]

@app.get("/api/students")
def get_students():
    return jsonify(students)

@app.get("/api/students/<int:id>")
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)

    return jsonify({"message": "Student not found"}), 404

@app.post("/api/students/<int:id>/enroll")
def enroll_student(id):

    data = request.json
    course_id = data.get("course_id")

    try:
        response = requests.get(
            f"http://localhost:5001/api/courses/{course_id}"
        )

        if response.status_code != 200:
            return jsonify({
                "message": "Course not found"
            }), 404

        return jsonify({
            "student_id": id,
            "course_id": course_id,
            "message": "Enrollment successful"
        })

    except requests.exceptions.ConnectionError:

        return jsonify({
            "message": "Course Service unavailable"
        }), 503


if __name__ == "__main__":
    app.run(port=5002, debug=True)