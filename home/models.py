from django.db import models
import accounts.models as account_model
import datetime
# Create your models here.

class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    dept_name = models.ForeignKey(account_model.Department, on_delete=models.CASCADE) 
    faculty_name = models.ForeignKey(account_model.Faculty, on_delete=models.CASCADE)
    sem = models.ForeignKey(account_model.Semester, on_delete=models.CASCADE)
    Students = models.ManyToManyField(account_model.Student)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    def __str__(self):
        return str(self.subject_name ) + ' ' + str(self.dept_name) + ' faculty ' + str(self.faculty_name)

class Attendance(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    student = models.ForeignKey(account_model.Student, on_delete=models.CASCADE)
    attendance_date = models.DateField(default=datetime.date.today)
    status = models.CharField(max_length=250, choices = [('1','Present'),('2','Absent')] )
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.subject) + " Date " + str(self.attendance_date) + " student  " + str(self.student) 
