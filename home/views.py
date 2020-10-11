from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from classroom.settings import LOGIN_URL, LOGIN_REDIRECT_URL


def login(request):
    return HttpResponse("Login Page")


@login_required
def home(request):
    return HttpResponse("Home Page")