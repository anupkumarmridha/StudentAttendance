from django.db import models
from accounts.models import User, Student

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    def __str__(self):
        return str(self.course_name)  

class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=1) #need to give defauult course
    staff_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    def __str__(self):
        return str(self.subject_name)  
