from django import forms
from accounts.models import Student, Faculty, Department, Semester


try:
    depts = Department.objects.all().values_list("dept_name", "dept_name")
    dept_list = []
    for item in depts:
        dept_list.append(item)
except Exception as e:
    print(e)



class addStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            "user",
            "phone",
            "campusEmail",
            "gender",
            "profile_pic",
            "roll",
            "Department",
            "Semester",
        )
        widgets = {
            "user": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "user_id",
                    "type": "hidden",
                }
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Phone Number"}
            ),
            "campusEmail": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your Campus Email",
                }
            ),
            "gender": forms.Select(attrs={"class": "form-control"}),
            # "profile_pic": forms.FileInput(attrs={"class": "rounded_list"}),
            "roll": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Your Roll Number"}
            ),
            "Department": forms.Select(
                choices=dept_list, attrs={"class": "form-control"}
            ),
            "Semester": forms.Select(attrs={"class": "form-control"}),
        }


class updateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            "phone",
            "campusEmail",
            "gender",
            "profile_pic",
            "roll",
            "Department",
            "Semester",
        )
        widgets = {
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Phone Number"}
            ),
            "campusEmail": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your Campus Email",
                }
            ),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "profile_pic": forms.FileInput(attrs={"class": "rounded_list"}),
            "roll": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Your Roll Number"}
            ),
            "Department": forms.Select(
                choices=dept_list, attrs={"class": "form-control"}
            ),
            "Semester": forms.Select(attrs={"class": "form-control"}),
        }


class addFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ("user", "phone", "campusEmail", "gender", "profile_pic","Department")
        widgets = {
            "user": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "user_id",
                    "type": "hidden",
                }
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Phone Number"}
            ),
            "campusEmail": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your Campus Email",
                }
            ),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "profile_pic": forms.FileInput(attrs={"class": "rounded_list"}),
            "Department": forms.Select(
                choices=dept_list, attrs={"class": "form-control"}
            ),
        }


class updateFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ("user", "phone", "campusEmail", "gender", "profile_pic","Department")
        widgets = {
            "user": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "user_id",
                    "type": "hidden",
                }
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Phone Number"}
            ),
            "campusEmail": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your Campus Email",
                }
            ),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "Department": forms.Select(
                choices=dept_list, attrs={"class": "form-control"}
            ),
            # "profile_pic": forms.FileInput(attrs={"class": "rounded_list"}),
        }
