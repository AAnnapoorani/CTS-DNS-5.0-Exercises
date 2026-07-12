from flask import Flask, request
import requests

app = Flask(__name__)

COURSE_SERVICE = "http://localhost:5001"
STUDENT_SERVICE = "http://localhost:5002"


@app.route("/api/courses", methods=["GET"])
def get_courses():

    response = requests.get(
        f"{COURSE_SERVICE}/api/courses"
    )

    return response.json()


@app.route("/api/students", methods=["GET"])
def get_students():

    response = requests.get(
        f"{STUDENT_SERVICE}/api/students"
    )

    return response.json()


@app.route(
    "/api/students/<int:id>/enroll",
    methods=["POST"]
)
def enroll(id):

    response = requests.post(
        f"{STUDENT_SERVICE}/api/students/{id}/enroll",
        json=request.json
    )

    return response.json(), response.status_code


if __name__ == "__main__":
    app.run(
        port=5000,
        debug=True
    )