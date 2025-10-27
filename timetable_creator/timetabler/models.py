from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.base_user import BaseUserManager

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("Admin", "Admin"),
        ("Lecturer", "Lecturer"),
        ("Student", "Student"),
    )
    role = models.CharField(choices=ROLE_CHOICES, max_length=20)
    username = models.CharField(max_length=30, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    REQUIRED_FIELDS = ['email']

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, profile_photo=None, phone_number=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, profile_photo=profile_photo, phone_number=phone_number)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, username, password, **extra_fields)

class Lecturer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    department = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Course(models.Model):
    title = models.CharField(max_length=100)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.title}'

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    department = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Timetable(models.Model):
    DAYS_CHOICES = (
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
    )
    days = models.CharField(choices=DAYS_CHOICES, max_length=20)
    title = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    location = models.CharField(max_length=30)

@receiver(post_save, sender=CustomUser)
def create_related_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == "Lecturer":
            Lecturer.objects.create(user=instance)
        elif instance.role == "Student":
            Student.objects.create(user=instance)
