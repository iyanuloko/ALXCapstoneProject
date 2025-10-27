from django.urls import include, path
from .views import LecturerViewSet, CourseViewSet, StudentViewSet, TimetableViewSet
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import LoginView, LogoutView

router = DefaultRouter()
router.register('Lecturer', LecturerViewSet)
router.register('Course', CourseViewSet)
router.register('Student', StudentViewSet)
router.register('Timetable', TimetableViewSet)

urlpatterns = [
    path('', LoginView.as_view(template_name = "login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('timetabler/', include(router.urls)),
]