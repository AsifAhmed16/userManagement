from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from .models import Profile, Blog
from .decorators import *


@login_required(login_url="/login")
def index(request):
    blogs = {'blogs': Blog.objects.all()}
    return render(request, 'userManagement/index.html', blogs)


@login_required(login_url="/admin/login")
@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    if request.method == 'POST':
        body = request.POST['body']
        blog = Blog
        blog.body = body
        blog.save()
        if request.user is None or not request.user.is_staff:
            return HttpResponse("<h1>Unauthorized</h1>")
    return render(request, 'userManagement/blog.html')


def login_admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse("<h1>Unauthorized</h1>")
        if not user.is_staff:
            return HttpResponse("<h1>You are not an admin</h1>")
        else:
            login(request, user)
            return render(request, 'userManagement/index.html')
    return render(request, 'userManagement/login.html')


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return HttpResponse("<h1>Unauthorized</h1>")
        else:
            login(request, user)
            return render(request, 'userManagement/index.html')
    return render(request, 'userManagement/login.html')


def edit_user(request):
    if request.method == 'POST':
        user = request.user
        phone = request.POST['phone']
        address = request.POST['address']
        profile, created = Profile.objects.get_or_create(user=request.user)
        user.profile.phone = phone
        user.profile.address = address
    return render(request, 'userManagement/edit_user.html')


@unauthenticated_user
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        create_user = User.objects.create_user(username=username, password=password, email=email)
        user = User.objects.latest('id')
        profile, created = Profile.objects.get_or_create(user=user)
        user.profile.phone = phone
        user.profile.address = address
        user.save()
        group = Group.objects.get(name='client')
        user.groups.add(group)
        return redirect('login')
    return render(request, 'userManagement/register.html')


def logout_user(request):
    logout(request)
    return redirect('login')
