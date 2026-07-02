from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    hello_view,
    DepartmentListAPIView,
    DepartmentDetailAPIView,
    CourseViewSet,
    StudentViewSet,
    EnrollmentViewSet
)

router = DefaultRouter()
router.register(
    'courses',
    CourseViewSet
)
router.register(
    'students',
    StudentViewSet
)
router.register(
    'enrollments',
    EnrollmentViewSet
)

urlpatterns = [
    path('hello/', hello_view),
    path(
        'departments/',
        DepartmentListAPIView.as_view()
    ),
    path(
        'departments/<int:pk>/',
        DepartmentDetailAPIView.as_view()
    ),
]

urlpatterns += router.urls