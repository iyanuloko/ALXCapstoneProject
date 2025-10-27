from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Timetable, Student, Lecturer, Course, CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'role')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'date_of_birth', 'profile_photo', 'phone_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'date_of_birth', 'profile_photo', 'phone_number')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Timetable)
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Course)
# Register your models here.
