from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from accounts.EmailBackEnd import EmailBackEnd
from django.contrib.auth import login, logout
from accounts.models import User
from django.contrib import messages
from home import views
from accounts.studentView import viewStudentProfile


def handelSingup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        user_type = "2"
        # check for errorneous input
        print(user_type)

        if pass1 != pass2:
            messages.error(request, "Password do not match.")
            return redirect("handelSingup")

        # Create User

        try:
            myuser = User.objects.create_user(
                username=username,
                password=pass1,
                email=email,
                first_name=fname,
                last_name=lname,
                user_type=user_type,
            )
            # myuser.is_active = False
            myuser.save()
            
            # print("here")
            messages.success(request, "Account Created Successfully!")
            return redirect(views.homeView)

        except Exception as e:
            print(e)
            messages.error(request, "Failed to SignUp!")
            return redirect(views.homeView)
    else:
        return HttpResponse("404 - Not Found")


def handleLogin(request):
    if request.method != "POST":
        return HttpResponse("Submission outside this window is not allowed 😎")
    else:
        # Get the post parameters
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]
        user = EmailBackEnd.authenticate(
            request, username=loginusername, password=loginpassword
        )
        if user is not None:
            login(request, user)
            messages.success(request, "Successfuly logged in 🥰")
            return redirect(views.homeView)
        else:
            messages.error(request, "Invalid credentialsl, Please try again 😎")
            return redirect(views.homeView)


def handleLogout(request):
    if request.method == "POST":
        value = request.POST["value"]
        logout(request)
        messages.success(request, "Successfuly logged out 🥰")

        return redirect(views.homeView)
    else:
             return HttpResponse("Sorry No Users Logged in 😎")
