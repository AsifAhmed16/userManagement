from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate


def login(request):
    if request.user.username == 'asif':
        return HttpResponse("<h1>Auth</h1>")
    return HttpResponse("<h1>Unauth</h1>")


def dashboard(request):
    if request.user.username == 'asif':
        return HttpResponse("<h1>Auth</h1>")
    return HttpResponse("<h1>Unauth</h1>")
