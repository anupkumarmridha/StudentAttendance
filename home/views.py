from django.shortcuts import render, redirect
from home.forms import addSubjectForm
from accounts.models import Faculty, Student
from django.contrib import messages
# Create your views here.

# Create your views here.
def homeView(request):
    return render(request, "home/index.html")

def viewSubject(request):
    return render(request, "home/viewSubject.html")

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
                return redirect('viewSubject')
            else:
                print("ERROR : Form is invalid")
                messages.error(request, "ERROR : Form is invalid!")
                print(form.errors)
    else:
        form = addSubjectForm()
    context = {"form": form}        
    return render(request, "home/addSubject.html", context=context)
    