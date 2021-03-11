from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile


@login_required(login_url="/login")
def dashboard(request):
    if request.user.username == 'asif':
        return HttpResponse("<h1>Auth</h1>")
    return HttpResponse("<h1>Unauth</h1>")


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse("<h1>Unauth</h1>")
    return render(request, 'userManagement/login.html')


# @login_required()
# def edit_user(request):
#     if request.method=='POST':
#         user = request.user
#         phone = "1234"
#         address = 'abcd, bd'
#         profile, created = Profile.objects.get_or_create(user=request.user)
#     user = authenticate(username=username, password=password)
#     if user is None:
#         return HttpResponse("<h1>Unauth</h1>")
#     else:
#         login(request, user)
#         return redirect('/')


def register(request):
    username = 'asif'
    password = '1234'
    email = 'r@g.c'
    created = User.objects.create_user(username=username, password=password, email=email)
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponse("<h1>Unauth</h1>")
    else:
        login(request, user)
        return redirect('/')


def logout_user(request):
    username = 'asif'
    password = '1234'
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponse("<h1>Unauth</h1>")
    else:
        return HttpResponse("<h1>Auth</h1>")
