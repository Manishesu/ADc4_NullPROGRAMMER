
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import House
from django.template import Template, Context
from django.contrib import messages
from django.http import HttpResponse


def index(request):
    return render(request, template_name="Home.html",)


def register_user(request):
    if request.method == "GET":
        return render(request, 'Registration/register.html')

    elif request.method == "POST":

        Username = request.POST['input_username']
        Password1 = request.POST['input_password1']
        Password2 = request.POST['input_password2']
        Email = request.POST['input_email']

        if Password1 == Password2:
            if User.objects.filter(username=Username).exists():
                messages.info(request, 'Username exists!!!')
                return render(request, 'Registration/register.html')

            elif User.objects.filter(email=Email).exists():
                messages.info(request, 'Email exists!!!')
                return render(request, 'Registration/register.html')

            else:
                user_obj = User.objects.create_user(username=Username, password=Password1, email=Email)
                user_obj.save()
                return HttpResponse("Signup Successful")
        else:
            messages.info(request, 'Password do not match!!!')
            return render(request, 'Registration/register.html')


def authenticate_user(request):
    if request.method == "GET":
        return render(request, 'Registration/login.html')

    else:
        user = authenticate(username=request.POST['input_username'], password=request.POST['input_password'])
        if user is not None:
            login(request, user)
            return render(request, 'bookings.html')
        else:
            messages.info(request, 'invalid username or password')
            return render(request, 'Registration/login.html')

