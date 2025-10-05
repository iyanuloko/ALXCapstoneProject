from django.shortcuts import render
from rest_framework import generics
from .models import Lecturer, Course
from .serializers import LecturerSerializer, CourseSerializer

class LecturerCreateAPIView(generics.CreateAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer

class CourseCreateAPIView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
# Create your views here.
