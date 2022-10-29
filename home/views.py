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
    student_longitude = request.session.get('student_longitude')
    student_latitude = request.session.get('student_latitude')
    faculty_longitude = request.session.get('faculty_longitude')
    faculty_latitude = request.session.get('faculty_latitude')
        
    print(student_longitude)
    print(student_latitude)
    print(faculty_longitude)
    print(faculty_latitude)
    return render(request, "home/index.html")


# def getLocation(request):
#     stu_lang = request.COOKIES.get('stu_lang')
#     print(stu_lang)

#     if request.method=='POST':   
#         stu_lang = request.POST.get("stu_lang")
#         stu_lat = request.POST.get("stu_lat")
#         faculty_lang = request.POST.get("faculty_lang")
#         faculty_lat = request.POST.get("faculty_lat")
#         # print(stu_lang)
#         # print(stu_lat)
#         # print(faculty_lang)
#         # print(faculty_lat)
#         request.session['stu_lang'] = stu_lang
#         request.session['stu_lat'] = stu_lat
#         request.session['faculty_lang'] = faculty_lang
#         request.session['faculty_lat'] = faculty_lat
#         messages.success(request, "Your Current Location is send ")    

#     return render(request, "location.html")

def viewAttendance(request):
    user=request.user
    student=Student.objects.get(user=user)
    attendance=Attendance.objects.filter(student=student)

    context={
        "attendance":attendance
    }
    print(context)
    return render(request, "home/viewAttendance.html", context=context)


def addAttendance(request):
    user=request.user
    try:
        student=Student.objects.get(user=user)
    except Exception as e:
        print(e)
    if request.method == 'POST':

        student_longitude = request.session.get('student_longitude')
        student_latitude = request.session.get('student_latitude')
        faculty_longitude = request.session.get('faculty_longitude')
        faculty_latitude = request.session.get('faculty_latitude')
        
        print(student_longitude)
        print(student_latitude)
        print(faculty_longitude)
        print(faculty_latitude)
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

                if(student_latitude==faculty_latitude or student_longitude==faculty_longitude):
                    obj.status="1"
                    obj.save() # Save the final "real form" to the DB
                    messages.success(request, "Attendance added Successfully!")
                else:
                    messages.error(request, "Location not matched!")
    else:
        form = addAttendanceForm()
    context = {"form": form}  
    return render(request, "home/addAttendance.html",context=context)



def subjects(request):
    student_longitude = request.session.get('student_longitude')
    student_latitude = request.session.get('student_latitude')
    faculty_longitude = request.session.get('faculty_longitude')
    faculty_latitude = request.session.get('faculty_latitude')
    
    print(student_longitude)
    print(student_latitude)
    print(faculty_longitude)
    print(faculty_latitude)
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
    