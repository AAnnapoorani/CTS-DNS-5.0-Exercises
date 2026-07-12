# API Versioning Strategies
# 1. URL Versioning:
#    /api/v1/courses/
#
# 2. Header Versioning:
#    Accept: application/vnd.api+json;version=1
#
# URL versioning is simpler and easier to test.
# Header versioning keeps URLs cleaner but requires
# clients to send custom headers.

from urllib import response
from django import db
from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi import BackgroundTasks
from fastapi import Response
from fastapi.security import OAuth2PasswordBearer

from security import verify_token

from regex import search
from sqlalchemy.orm import Session

from database import Base
from database import engine
from database import get_db

from fastapi.middleware.cors import CORSMiddleware

from models import (
    Course,
    Student,
    Enrollment,
    User
)

from schemas import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
    StudentCreate,
    StudentResponse,
    EnrollmentCreate,
    EnrollmentResponse,
    UserCreate,
    UserResponse,
    LoginRequest,
    TokenResponse
)

from security import (
    get_password_hash,
    verify_password,
    create_access_token
)

app = FastAPI(
    title="Course Management API",
    description="Course Management System using FastAPI",
    version="1.0.0",
    contact={
        "name": "Annapoorani",
        "email": "annapoorani@example.com"
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
    )

# OAuth2 Authorization Code Flow:
# User authenticates through an authorization server, receives an authorization code, exchanges it for an access token.

# JWT Login implemented here is simpler:
# User directly submits credentials and receives a JWT token. No authorization server or authorization code exchange is involved.

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
    "/api/v1/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"],
    summary="Create Course",
    response_description="Course created successfully"
)
async def create_course(
    course: CourseCreate,
    response: Response,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):

    verify_token(token)

    new_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    response.headers["Location"] = (
        f"/api/v1/courses/{new_course.id}"
    )

    return new_course

@app.get(
    "/api/v1/courses/{course_id}",
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
            detail={
                "error": {
                    "code": "NOT_FOUND",
                    "message": "Course not found",
                    "field": None
                }
            }
        )

    return course

@app.get(
    "/api/v1/courses/",
    response_model=dict,
    tags=["Courses"],
    summary="Get All Courses"
)
async def get_courses(
    page: int = 1,
    page_size: int = 2,
    department_id: int = None,
    search: str = None,
    db: Session = Depends(get_db)
):

    query = db.query(Course)

    if search:
        query = query.filter(
            Course.name.ilike(f"%{search}%")
        )

    if department_id:
        query = query.filter(
            Course.department_id == department_id
    )

    total = query.count()

    courses = query.offset(
        (page - 1) * page_size
    ).limit(
        page_size
    ).all()

    next_page = None
    if page * page_size < total:
        next_page = page + 1

    previous_page = None
    if page > 1:
        previous_page = page - 1

    return {
    "count": total,
    "next": next_page,
    "previous": previous_page,
    "results": [
        {
            "id": course.id,
            "name": course.name,
            "code": course.code,
            "credits": course.credits,
            "department_id": course.department_id
        }
        for course in courses
    ]
}

@app.put(
    "/api/v1/courses/{course_id}",
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
            detail={
                "error": {
                    "code": "NOT_FOUND",
                    "message": "Course not found",
                    "field": None
        }
    }
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

@app.patch(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"]
)
async def patch_course(
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
            detail={
                "error": {
                    "code": "NOT_FOUND",
                    "message": "Course not found",
                    "field": None
                }
            }
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
    "/api/v1/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Courses"],
    summary="Delete Course"
)
async def delete_course(
    course_id: int,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):

    verify_token(token)

    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail={
                "error": {
                    "code": "NOT_FOUND",
                    "message": "Course not found",
                    "field": None
                }
            }
        )

    db.delete(course)
    db.commit()

@app.post(
    "/api/v1/students/",
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
    "/api/v1/enrollments/",
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
            detail={
                "error": {
                    "code": "NOT_FOUND",
                    "message": "Student not found",
                    "field": None
                }
            }
        )

    course = db.query(Course).filter(
        Course.id == enrollment.course_id
    ).first()

    if not course:
        raise HTTPException(
    status_code=404,
    detail={
        "error": {
            "code": "NOT_FOUND",
            "message": "Course not found",
            "field": None
        }
    }
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
    "/api/v1/courses/{course_id}/students",
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
    detail={
        "error": {
            "code": "NOT_FOUND",
            "message": "Course not found",
            "field": None
        }
    }
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

@app.post(
    "/api/v1/auth/register/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Authentication"],
    summary="Register User"
)
async def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    hashed_password = get_password_hash(
        user.password
    )

    new_user = User(
        email=user.email,
        hashed_password=hashed_password,
        is_active=True
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.get("/debug/users")
async def debug_users(
    db: Session = Depends(get_db)
):
    users = db.query(User).all()

    return [
        {
            "id": user.id,
            "email": user.email,
            "hashed_password": user.hashed_password
        }
        for user in users
    ]

@app.post(
    "/api/v1/auth/login/",
    response_model=TokenResponse,
    tags=["Authentication"],
    summary="User Login"
)
async def login_user(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == credentials.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        credentials.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        data={
            "sub": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.get(
    "/api/v1/protected",
    tags=["Authentication"]
)
async def protected_route(
    token: str = Depends(oauth2_scheme)
):

    email = verify_token(token)

    return {
        "message": "Access granted",
        "user": email
    }