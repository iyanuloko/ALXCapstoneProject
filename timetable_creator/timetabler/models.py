from django.db import models
class Lecturer(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
# Create your models here.
