from fastapi import FastAPI
from fastapi import Depends

from sqlalchemy.orm import Session

from database import Base
from database import engine
from database import get_db

from models import Course

from schemas import (
    CourseCreate,
    CourseResponse
)

app = FastAPI(
    title="Course Management API",
    version="1.0"
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "API running"
    }


@app.post(
    "/api/courses/",
    response_model=CourseResponse
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
    response_model=CourseResponse
)
async def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):

    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    return course

@app.get("/api/courses/")
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