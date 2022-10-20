from accounts.models import Student, User
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect

def viewStudentProfile(request):
    try:
        user=request.user
        studentProfile = Student.objects.filter(user=user)
        context={
        'studentDetails': studentProfile
        }
        return render(request, "student/studentDashboard.html", context)
    except Exception as e:
        print(e)
        messages.error(request, "Student profile not found")
        print(e)
    return render(request, "student/studentDashboard.html")