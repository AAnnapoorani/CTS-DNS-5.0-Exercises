from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi import BackgroundTasks

from sqlalchemy.orm import Session

from database import Base
from database import engine
from database import get_db

from models import (
    Course,
    Student,
    Enrollment
)

from schemas import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
    StudentCreate,
    StudentResponse,
    EnrollmentCreate,
    EnrollmentResponse
)

app = FastAPI(
    title="Course Management API",
    description="Course Management System using FastAPI",
    version="1.0.0",
    contact={
        "name": "Annapoorani",
        "email": "annapoorani@example.com"
    }
)

Base.metadata.create_all(bind=engine)

def send_confirmation_email(student_email: str):
    print(
        f"Sending confirmation email to {student_email}"
    )

@app.get("/")
def root():
    return {
        "message": "API running"
    }

@app.post(
    "/api/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"],
    summary="Create Course",
    response_description="Course created successfully"
)
async def create_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):

    new_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course

@app.get(
    "/api/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"],
    summary="Get Course By ID"
)
async def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):

    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course

@app.get(
    "/api/courses/",
    response_model=list[CourseResponse],
    tags=["Courses"],
    summary="Get All Courses"
)
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: int = None,
    db: Session = Depends(get_db)
):

    query = db.query(Course)

    if department_id:
        query = query.filter(
            Course.department_id == department_id
        )

    courses = query.offset(skip).limit(limit).all()

    return courses

@app.put(
    "/api/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"],
    summary="Update Course"
)
async def update_course(
    course_id: int,
    course_data: CourseUpdate,
    db: Session = Depends(get_db)
):

    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    if course_data.name is not None:
        course.name = course_data.name
    if course_data.code is not None:
        course.code = course_data.code
    if course_data.credits is not None:
        course.credits = course_data.credits
    if course_data.department_id is not None:
        course.department_id = course_data.department_id

    db.commit()
    db.refresh(course)

    return course

@app.delete(
    "/api/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Courses"],
    summary="Delete Course"
)
async def delete_course(
    course_id: int,
    db: Session = Depends(get_db)
):

    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    db.delete(course)
    db.commit()

@app.post(
    "/api/students/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Students"],
    summary="Create Student"
)
async def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    new_student = Student(
        name=student.name,
        email=student.email
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

@app.post(
    "/api/enrollments/",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Enrollments"],
    summary="Create Enrollment"
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == enrollment.student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    course = db.query(Course).filter(
        Course.id == enrollment.course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    new_enrollment = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id
    )

    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)

    background_tasks.add_task(
        send_confirmation_email,
        student.email
    )

    return new_enrollment

@app.get(
    "/api/courses/{course_id}/students",
    response_model=list[StudentResponse],
    tags=["Enrollments"],
    summary="Get Students Enrolled In Course"
)
async def get_course_students(
    course_id: int,
    db: Session = Depends(get_db)
):

    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    enrollments = db.query(Enrollment).filter(
        Enrollment.course_id == course_id
    ).all()

    students = []

    for enrollment in enrollments:

        student = db.query(Student).filter(
            Student.id == enrollment.student_id
        ).first()

        if student:
            students.append(student)

    return students