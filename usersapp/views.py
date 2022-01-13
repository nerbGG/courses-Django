from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# use this to create users
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
# import the users table
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.
def register(response):
    # if response.method == "POST":
    #     # form = UserCreationForm(response.POST) #creates a user
    #     form = RegisterForm(response.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect("/")
    # else:
    #     form = RegisterForm()
    # return render(response, "usersapp/register.html", {"form": form})
    return render(response, "usersapp/register.html")


def createuser(response):
    firstname = response.POST['first_name']
    lastname = response.POST['last_name']
    username = response.POST['username']
    email = response.POST['email']
    password = response.POST['password']
    try:
        user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email, password=password)
        user.save()
    except Exception:
        return HttpResponse('<h1> user already exists</h1><a href="../register/">previous page</a>')

    return redirect("/")
