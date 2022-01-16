from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
# use this to create users
# from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect

from .forms import RegisterForm
# import the users table
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.
# def register(response):
# if response.method == "POST":
#     # form = UserCreationForm(response.POST) #creates a user
#     form = RegisterForm(response.POST)
#     if form.is_valid():
#         form.save()
#     return redirect("/")
# else:
#     form = RegisterForm()
# return render(response, "usersapp/register.html", {"form": form})

def register(response):
    # can access the current user here
    # response.user
    if response.method == "POST":
       return createuser(response)
    else:
        return render(response, "usersapp/register.html", {"useralreadyexists": False})


def createuser(response):
    firstname = response.POST['first_name']
    lastname = response.POST['last_name']
    username = response.POST['username']
    email = response.POST['email']
    password = response.POST['password']
    try:
        user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,
                                       password=password)
        user.save()
    except Exception:
        return render(response, "usersapp/register.html", {"useralreadyexists": True})

    return redirect("/login")


def loginpage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, "registration/login.html", {'error': True})
    else:
        return render(request, "registration/login.html", {'error': False})


def logoutuser(response):
    logout(response)
    return redirect("/")
