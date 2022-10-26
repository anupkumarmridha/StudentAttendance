from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    user_type_data = (("1", "Student"), ("2", "Faculty"))
    # user_type = models.CharField(choices=user_type_data, max_length=20)
    user_type = models.CharField(default='1',choices=user_type_data, max_length=20)


class Department(models.Model):
    dept_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.dept_name)


class Semester(models.Model):
    sem_choice = (
        ("1", "First Semester"),
        ("2", "Second Semester"),
        ("3", "Third Semester"),
        ("4", "Fourth Semester"),
        ("5", "Fifth Semester"),
        ("6", "Six Semester"),
        ("7", "Seven Semester"),
        ("8", "Eight Semester"),
    )
    sem = models.CharField(choices=sem_choice, max_length=255)

    def __str__(self):
        return str(self.sem)


class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13, blank=True, null=True)
    campusEmail = models.CharField(max_length=255, blank=True, null=True)
    gender_choice = (("M", "Male"), ("F", "Female"))
    gender = models.CharField(choices=gender_choice, max_length=20)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_hod = models.BooleanField(default=False)
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="images/Facultys/profile/"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.user)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13, blank=True, null=True)
    campusEmail = models.CharField(max_length=255, blank=True, null=True)
    gender_choice = (("M", "Male"), ("F", "Female"))
    gender = models.CharField(choices=gender_choice, max_length=20)
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="images/Students/profile/"
    )
    roll = models.CharField(max_length=9, unique=True)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.user)
