from django.shortcuts import render
from django.http import HttpResponse

from .models import Classroom, Test, Question, Choice

# Create your views here.
def home(request):
    classrooms = Classroom.objects.all()
    return HttpResponse(classrooms)
