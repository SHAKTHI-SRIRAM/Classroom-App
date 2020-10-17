from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def teacher_home(request):
    return HttpResponse('Teacher Page')