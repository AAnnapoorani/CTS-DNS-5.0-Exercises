"""
TASK 1

REQUEST -> RESPONSE CYCLE IN DJANGO

User enters:
http://127.0.0.1:8000/api/courses/

1. Browser sends HTTP Request
2. Django URL Router checks urls.py
3. Matching View function/class is called
4. View interacts with Model
5. Model queries Database
6. Database returns data
7. View processes data
8. Response object is created
9. Browser receives HTTP Response
"""

"""
MIDDLEWARE

Middleware sits between Request and View.

Examples:

1. SecurityMiddleware
   Adds security headers and protections.

2. AuthenticationMiddleware
   Associates logged-in user information with requests.
"""

"""
WSGI vs ASGI

WSGI:
- Web Server Gateway Interface
- Handles synchronous requests
- Traditional Django

ASGI:
- Asynchronous Server Gateway Interface
- Supports WebSockets
- Supports Async Views
- Better for real-time applications

Django uses:
WSGI by default

Use ASGI when:
- WebSockets
- Chat applications
- Live notifications
- Async APIs
"""

"""
MVC vs MVT

MVC:
Model
View
Controller

Django MVT:

Model -> Model
View -> Controller
Template -> View

Mapping:

MVC Model      = Django Model
MVC View       = Django Template
MVC Controller = Django View
"""

""" Browser ----> URL Router ----> View ----> Model ----> Database ----> View ----> Response ----> Browser """