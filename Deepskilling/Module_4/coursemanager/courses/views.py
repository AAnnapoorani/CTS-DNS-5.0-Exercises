from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Department, Enrollment
from .serializers import DepartmentSerializer
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer
from .models import Enrollment
from .serializers import EnrollmentSerializer
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

def hello_view(request):
    return HttpResponse(
        "Course Management API is running"
    )

class DepartmentListAPIView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(
            departments,
            many=True
        )
        return Response(serializer.data)
    def post(self, request):
        serializer = DepartmentSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=201
            )
        return Response(
            serializer.errors,
            status=400
        )

class DepartmentDetailAPIView(APIView):
    def get(self, request, pk):
        department = Department.objects.get(pk=pk)
        serializer = DepartmentSerializer(
            department
        )
        return Response(serializer.data)
    def put(self, request, pk):
        department = Department.objects.get(pk=pk)
        serializer = DepartmentSerializer(
            department,
            data=request.data
        )
        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=400
        )
    def delete(self, request, pk):
        department = Department.objects.get(pk=pk)
        department.delete()
        return Response(
            {
                "message":
                "Department deleted successfully"
            },
            status=204
        )

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    @action(
        detail=True,
        methods=['get']
    )
    def students(self, request, pk=None):
        course = self.get_object()
        enrollments = Enrollment.objects.filter(
            course=course
        )
        students = [
            enrollment.student
            for enrollment in enrollments
        ]
        serializer = StudentSerializer(
            students,
            many=True
        )
        return Response(
            serializer.data
        )

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer