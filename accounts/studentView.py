from accounts.models import Student
from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.forms import addStudentForm, updateStudentForm
from django.views.generic import UpdateView
from django.urls import reverse

def viewStudentProfile(request):
    try:
        user=request.user
        studentProfile = Student.objects.filter(user=user)
        print(studentProfile)
        context={
        'studentDetails': studentProfile
        }
        return render(request, "student/studentDashboard.html", context)
    except Exception as e:
        # print(e)
        messages.error(request, "Student profile not found")
        print(e)
    return render(request, "student/studentDashboard.html")

def addStudent(request):
    if request.method == "POST":
        try:
            form = addStudentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Student info added successfully")
                return redirect(viewStudentProfile)
            else:
                messages.error(request, "Form is Not Valid")
        except Exception as e:
            print(e)
    else:
        form = addStudentForm()
    context = {"form": form}
    return render(request, "student/addStudent.html", context=context)

class updateStudent(UpdateView):
    model = Student
    form_class = updateStudentForm
    template_name = "student/updateStudent.html"

    def get_success_url(self):
        messages.success(self.request, "Student info updated successfully")
        return reverse(viewStudentProfile)