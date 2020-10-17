from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def teacher_home(request):
    if request.user.is_staff or request.user.is_superuser:
        return HttpResponse('Teacher Page')
    else:
        return HttpResponse('''
        You are not authenticated to view this page. Please contact the admin to get staff status.''')
