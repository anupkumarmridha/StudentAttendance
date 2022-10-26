from accounts.models import Faculty
from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.forms import addFacultyForm, updateFacultyForm
from django.views.generic import UpdateView
from django.urls import reverse


def viewFacultyProfile(request):
    try:
        user = request.user
        facultyProfile = Faculty.objects.filter(user=user)
        print(facultyProfile)
        context = {"facultyDetails": facultyProfile}
        return render(request, "faculty/facultyDashboard.html", context)
    except Exception as e:
        # print(e)
        messages.error(request, "Faculty profile not found")
        print(e)
    return render(request, "faculty/facultyDashboard.html")


def addFaculty(request):
    if request.method == "POST":
        try:
            form = addFacultyForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Faculty info added successfully")
                return redirect(viewFacultyProfile)
            else:
                messages.error(request, "Form is Not Valid")
        except Exception as e:
            print(e)
    else:
        form = addFacultyForm()
    context = {"form": form}
    return render(request, "faculty/addFaculty.html", context=context)


class updateFaculty(UpdateView):
    model = Faculty
    form_class = updateFacultyForm
    template_name = "faculty/updateFaculty.html"

    def get_success_url(self):
        messages.success(self.request, "Faculty info updated successfully")
        return reverse(viewFacultyProfile)
