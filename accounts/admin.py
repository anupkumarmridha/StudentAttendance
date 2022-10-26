from django.contrib import admin

# Register your models here.
from accounts.models import User, Student, Faculty, Department, Semester
# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Semester)
