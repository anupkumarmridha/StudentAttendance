from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    user_type_data = ((1, "HOD"),(2, "Student"), (3, "Faculty"))
    # user_type = models.CharField(choices=user_type_data, max_length=20)
    user_type = models.CharField(default=1, choices=user_type_data, max_length=20)


class Hod(models.Model):
    hod = models.OneToOneField(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    def __str__(self):
        return str(self.hod)    

class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone=models.CharField(max_length=13, blank=True, null=True)
    campusEmail= models.CharField(max_length=255, blank=True, null=True)
    gender_choice=(('M',"Male"),('F',"Female"))
    gender = models.CharField(choices=gender_choice, max_length=20)
    profile_pic = models.ImageField(null=True, blank=True,upload_to='images/Students/profile/')
    dob = models.DateField()
    fid=models.CharField(max_length=9, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.user)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone=models.CharField(max_length=13, blank=True, null=True)
    campusEmail= models.CharField(max_length=255, blank=True, null=True)
    gender_choice=(('M',"Male"),('F',"Female"))
    gender = models.CharField(choices=gender_choice, max_length=20)
    profile_pic = models.ImageField(null=True, blank=True,upload_to='images/Students/profile/')
    dob = models.DateField()
    roll=models.CharField(max_length=9, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.user)
