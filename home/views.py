from logging import exception
from multiprocessing import context
from django.shortcuts import render, redirect
from home.forms import addSubjectForm, updateSubjectForm, addAttendanceForm
from accounts.models import Faculty, Student
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from home.models import Subject, Attendance

from django.views.generic import (
    UpdateView,
    DeleteView,
)

# Create your views here.
def homeView(request):
    try:
        user=request.user
        if(user.user_type == '1'):
            try:
                student=Student.objects.get(user=user)
            except Exception as e:
                messages.error(request,"Student dose not exist please add profile details")
                redirect(homeView)
            # get locations from coockeis            
            stu_lang = request.COOKIES.get('stu_lang')
            stu_lat = request.COOKIES.get('stu_lat')

            student.location_latitude=stu_lang
            student.location_longitude=stu_lat
            student.save()

        if(user.user_type == '2'):
            try:
                faculty=Faculty.objects.get(user=user)
            except Exception as e:
                messages.error(request,"Faculty dose not exist please add profile details")
                redirect(homeView)

            # get locations from coockeis   
            faculty_lang = request.COOKIES.get('faculty_lang')
            faculty_lat = request.COOKIES.get('faculty_lat')

            faculty.location_latitude=faculty_lang
            faculty.location_longitude=faculty_lat
            faculty.save()

    except Exception as e:
        pass
    return render(request, "home/index.html")


def viewAttendance(request):
    user=request.user
    context={}
    try:
        student=Student.objects.get(user=user)
        attendance=Attendance.objects.filter(student=student)   
        context={
            "attendance":attendance
        }
    except Exception as e:
        messages.error(request,"Student dose not exist please add profile details")
        redirect(homeView)
    return render(request, "home/viewAttendance.html", context=context)


def addAttendance(request):
    user=request.user
    try:
        student=Student.objects.get(user=user)
    except Exception as e:
        print(e)
    if request.method == 'POST':
        if request.user.is_authenticated:
            user=request.user
            try:
                student=Student.objects.get(user=user)       
            except Exception as e:
                messages.error(request, "Student details not found Please add Student Details from profile section.")
                return redirect(addAttendance)

            form = addAttendanceForm(request.POST)
            for field in form:
                print(field.value())
            if form.is_valid():
                obj = form.save(commit=False) # Return an object without saving to the DB
                obj.student=student
                try:
                    subject=Subject.objects.get(pk=obj.subject.id)
                    faculty=Faculty.objects.get(pk=subject.faculty_name.id)
                except Exception as e:
                    print(e)
                if(student.location_latitude==faculty.location_latitude or student.location_longitude==faculty.location_longitude):
                    obj.status="Present"
                    obj.save() # Save the final "real form" to the DB
                    messages.success(request, "Attendance added Successfully!")
                else:
                    messages.error(request, "Location not matched!")
    else:
        form = addAttendanceForm()
    context = {"form": form}  
    return render(request, "home/addAttendance.html",context=context)



def subjects(request):
    try:
        user=request.user
        if(user.user_type=='1'):
            student=Student.objects.get(user=user)
            subjects=Subject.objects.filter(Students=student)
        if(user.user_type=='2'):
            faculty=Faculty.objects.get(user=user)
            subjects=Subject.objects.filter(faculty_name=faculty)
    except Exception as e:
        messages.error(request,"No subjects were found")
        return redirect(homeView)
    context={
        "subjects": subjects,
    }
    return render(request, "home/subjects.html", context=context)

def viewSubject(request, pk):
    try:
        subject=Subject.objects.get(id=pk)
    except Exception as e:
        messages.error(request,"subject detail not found")
        print(e)
        redirect(subjects)
    context={
        "subject": subject,
    }
    return render(request, "home/viewSubject.html", context=context)

class updateSubject(UpdateView):
    model = Subject
    form_class = updateSubjectForm
    template_name = "home/updateSubject.html"

    def get_success_url(self):
        return reverse("subjects")

class DeletePostView(DeleteView):
    model=Subject
    template_name='product/delete_product.html'
    success_url=reverse_lazy('subjects')



def addSubject(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            user=request.user

            try:
                faculty=Faculty.objects.get(user=user)
                print(faculty.Department)       
            except Exception as e:
                messages.error(request, "Faculty details not found Please add faculty Details from profile section.")
                return redirect(addSubject)

            form = addSubjectForm(request.POST)
            for field in form:
                print(field.value())
            if form.is_valid():
                obj = form.save(commit=False) # Return an object without saving to the DB
                try:
                    students=Student.objects.filter(Semester=obj.sem, Department=faculty.Department)
                    print(students)
                except Exception as e:
                    print(e)
                obj.dept_name= faculty.Department
                obj.faculty_name = faculty 
                obj.save() # Save the final "real form" to the DB
                for item in students:
                    print(item)
                    obj.Students.add(item)
                messages.success(request, "Subject added Successfully!")
                return redirect('subjects')
            else:
                print("ERROR : Form is invalid")
                messages.error(request, "ERROR : Form is invalid!")
                print(form.errors)
    else:
        form = addSubjectForm()
    context = {"form": form}        
    return render(request, "home/addSubject.html", context=context)
    