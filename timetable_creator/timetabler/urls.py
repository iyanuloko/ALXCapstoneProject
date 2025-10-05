from django.urls import include, path
from .views import LecturerCreateAPIView, CourseCreateAPIView

urlpatterns = [
    path('lecturer/create/', LecturerCreateAPIView.as_view(), name='lecturer_create'),
    path('course/create/', CourseCreateAPIView.as_view(), name='course_create'),
]