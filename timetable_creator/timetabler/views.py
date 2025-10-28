from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Lecturer, Course, Student, Timetable
from .serializers import LecturerSerializer, CourseSerializer, StudentSerializer, TimetableSerializer
from django.contrib.auth.decorators import login_required
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Admin'

class IsLecturer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Lecturer'

class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Student'

class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    # block students and lecturers
    permission_classes = [IsAdmin, permissions.IsAuthenticated]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # block students from this view
    permission_classes = [(IsAdmin | IsLecturer), permissions.IsAuthenticated]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # block students and lecturers
    permission_classes = [IsAdmin, permissions.IsAuthenticated]

class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    # allow read only view for students and lecturers
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated()]
        return [IsAdmin()]

@login_required(login_url='login')
def timetable_view(request):
    timetable = Timetable.objects.select_related('title', 'lecturer').order_by('days', 'start_time')
    # Extract all distinct time slots (e.g., "08:00 - 10:00")
    time_slots = sorted({
        f"{t.start_time.strftime('%H:%M')} - {t.end_time.strftime('%H:%M')}"
        for t in timetable
    })
    # Group entries by day
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    timetable_dict = {day: {slot: None for slot in time_slots} for day in days}
    for t in timetable:
        time_label = f"{t.start_time.strftime('%H:%M')} - {t.end_time.strftime('%H:%M')}"
        timetable_dict[t.days][time_label] = t
    return render(request, 'timetable.html', {
        'timetable_dict': timetable_dict,
        'time_slots': time_slots,
    })

# Create your views here.
