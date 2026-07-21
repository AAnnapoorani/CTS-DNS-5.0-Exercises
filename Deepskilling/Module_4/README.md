# Module 4: Django REST Framework and FastAPI

## Overview
This module covers building robust REST APIs and microservices using two popular Python frameworks: Django REST Framework (DRF) and FastAPI. It includes hands-on projects demonstrating API design, authentication, database integration, and microservice architecture patterns.

## Module Structure
```
Module_4/
├── coursemanager/           # Django REST Framework project
│   ├── manage.py            # Django management script
│   ├── courses/             # Courses app
│   │   ├── models.py        # Database models
│   │   ├── views.py         # API views/viewsets
│   │   ├── serializers.py   # Request/response serializers
│   │   ├── urls.py          # URL routing
│   │   └── tests.py         # Test cases
│   └── settings.py          # Django settings
├── Hands_on_1/              # Basic API concepts
├── Hands_on_2/              # REST principles
├── Hands_on_3/              # Serialization
├── Hands_on_4/              # Authentication
├── Hands_on_5/              # Permissions
├── Hands_on_6/              # Viewsets and routers
├── Hands_on_7/              # Pagination and filtering
├── Hands_on_8/              # Database and relationships
│   ├── models.py            # SQLAlchemy models
│   ├── database.py          # Database configuration
│   └── schemas.py           # Pydantic schemas
├── Hands_on_9/              # FastAPI with authentication
│   ├── main.py              # FastAPI application
│   ├── models.py            # SQLAlchemy models
│   ├── database.py          # Database connection
│   ├── schemas.py           # Request/response schemas
│   └── security.py          # Authentication logic
├── Hands_on_10/             # Microservices architecture
│   ├── gateway/             # API Gateway
│   │   └── app.py
│   ├── student_service/     # Student microservice
│   │   └── app.py
│   ├── course_service/      # Course microservice
│   │   └── app.py
│   └── docker-compose.yml   # Container orchestration
└── Output/                  # Output files directory
```

## Topics Covered

### Django REST Framework
- Model creation and relationships
- Serializers and validation
- APIView and ViewSets
- Generic views and mixins
- URL routing and routers
- Authentication and permissions
- Pagination, filtering, and searching
- Testing and error handling

### FastAPI
- Path parameters and query parameters
- Request and response models
- Status codes and error handling
- Dependency injection
- Middleware
- Authentication and authorization
- Database integration
- API documentation (OpenAPI/Swagger)

### Microservices Architecture
- Service discovery
- API Gateway pattern
- Inter-service communication
- Docker containerization
- Service scaling

## Getting Started

### Prerequisites
- Python 3.8 or higher
- PostgreSQL or MySQL
- Docker and Docker Compose (for microservices)
- Basic REST API knowledge
- Understanding of OOP and databases

### Installation

#### For Django Project
```bash
# Install dependencies
pip install -r requirements.txt

# Set up database
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

#### For FastAPI Projects
```bash
# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
uvicorn main:app --reload

# Or for specific hands_on
cd Hands_on_9
uvicorn main:app --reload --port 8001
```

#### For Microservices
```bash
# Start all services with Docker Compose
docker-compose up

# Services will be available at:
# - API Gateway: http://localhost:8000
# - Student Service: http://localhost:8001
# - Course Service: http://localhost:8002
```

## Usage

### Django REST Framework Example
```python
# models.py
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# serializers.py
from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'created_at']

# views.py
from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

### FastAPI Example
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Course(BaseModel):
    name: str
    description: str

# GET all courses
@app.get("/courses", response_model=List[Course])
async def get_courses():
    return courses

# POST create course
@app.post("/courses", response_model=Course)
async def create_course(course: Course):
    courses.append(course)
    return course

# GET single course
@app.get("/courses/{course_id}", response_model=Course)
async def get_course(course_id: int):
    if course_id < len(courses):
        return courses[course_id]
    raise HTTPException(status_code=404, detail="Course not found")

# PUT update course
@app.put("/courses/{course_id}", response_model=Course)
async def update_course(course_id: int, course: Course):
    if course_id < len(courses):
        courses[course_id] = course
        return course
    raise HTTPException(status_code=404, detail="Course not found")

# DELETE course
@app.delete("/courses/{course_id}")
async def delete_course(course_id: int):
    if course_id < len(courses):
        courses.pop(course_id)
        return {"message": "Course deleted"}
    raise HTTPException(status_code=404, detail="Course not found")
```

## API Endpoints Reference

### Django REST Framework Course Manager
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/courses/` | List all courses |
| POST | `/api/courses/` | Create new course |
| GET | `/api/courses/{id}/` | Retrieve course |
| PUT | `/api/courses/{id}/` | Update course |
| DELETE | `/api/courses/{id}/` | Delete course |

### FastAPI Hands_on_9
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/token` | Get access token |
| GET | `/users/me` | Get current user |
| POST | `/users/` | Create user |

## Learning Objectives
- Build REST APIs using Django REST Framework
- Create modern APIs with FastAPI
- Implement authentication and authorization
- Design microservice architectures
- Handle database relationships and queries
- Validate request/response data
- Test API endpoints
- Deploy services with Docker

## Django vs FastAPI Comparison

| Feature | Django REST | FastAPI |
|---------|------------|---------|
| Learning Curve | Medium | Easy |
| Performance | Good | Excellent |
| Setup Time | Moderate | Fast |
| Built-in Admin | Yes | No |
| Type Hints | Optional | Required |
| Async Support | Limited | Full |
| Documentation | Auto-generated | Auto-generated |

## Authentication Methods

### JWT (JSON Web Token)
```python
# FastAPI example
from fastapi.security import HTTPBearer, HTTPAuthCredentials
from jose import JWTError, jwt

security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return username
```

### Session-based (Django)
```python
# Django uses session middleware automatically
# Just use @login_required decorator
```

## Testing APIs

### Using curl
```bash
# GET request
curl http://localhost:8000/api/courses/

# POST request
curl -X POST http://localhost:8000/api/courses/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Python 101","description":"Learn Python"}'

# With authentication
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:8000/api/courses/
```

### Using Python requests
```python
import requests

# GET
response = requests.get('http://localhost:8000/api/courses/')
courses = response.json()

# POST
data = {"name": "Python 101", "description": "Learn Python"}
response = requests.post('http://localhost:8000/api/courses/', json=data)
new_course = response.json()
```

## Output Files
- API documentation auto-generated at `/docs` (FastAPI Swagger UI)
- Database logs and test results in `Output/` directory
- Service logs in microservices deployment

## Best Practices
1. Use version control for APIs (`/api/v1/`, `/api/v2/`)
2. Implement proper error handling and validation
3. Use pagination for large datasets
4. Implement rate limiting
5. Add request/response logging
6. Write comprehensive tests
7. Document API endpoints
8. Use HTTPS in production
9. Implement CORS properly
10. Monitor API performance

## HTTP Status Codes
- **200 OK**: Successful GET request
- **201 Created**: Successful POST request
- **204 No Content**: Successful DELETE request
- **400 Bad Request**: Invalid request format
- **401 Unauthorized**: Authentication required
- **403 Forbidden**: Permission denied
- **404 Not Found**: Resource not found
- **500 Server Error**: Internal server error

## Troubleshooting

### Django Migrations Issues
```bash
# Reset migrations (development only)
python manage.py migrate courses zero
python manage.py makemigrations
python manage.py migrate
```

### CORS Issues
```python
# Add to Django settings
INSTALLED_APPS = [
    'corsheaders',
]
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

### FastAPI Database Connection
- Verify database server is running
- Check connection string in database.py
- Ensure database driver is installed

## Further Reading
- Django REST Framework Official Docs
- FastAPI Official Documentation
- REST API Best Practices
- Microservices Architecture Patterns
- API Security Guidelines

## Notes
- Each hands_on builds on previous concepts
- Start with hands_on_1 for basics
- Hands_on_10 demonstrates advanced patterns
- Run tests before deployment
- Use environment variables for sensitive data

## Author
CTS DNS 5.0 Exercises

## License
Educational - Use for learning purposes
