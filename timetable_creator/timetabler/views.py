from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import Lecturer, Course, Student
from .serializers import LecturerSerializer, CourseSerializer, StudentSerializer

# block students and lecturers (only admin)
class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer

# block students from this view
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# block students and lecturers
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# Create your views here.
