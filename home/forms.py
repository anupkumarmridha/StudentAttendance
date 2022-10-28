from urllib import request
from django import forms
from accounts.models import User, Student, Faculty, Department, Semester
from home.models import Subject


class addSubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = (
            "subject_name",
            "sem",
        )
        widgets = {
            "subject_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "sem": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
        }

class updateSubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = (
            "subject_name",
            "sem",
            "Students",
        )
        widgets = {
            "subject_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "sem": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "Students": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
        }
