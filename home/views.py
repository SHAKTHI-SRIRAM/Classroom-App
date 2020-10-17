from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from classroom.settings import LOGIN_URL, LOGIN_REDIRECT_URL
from .forms import UserRegisterForm


@login_required
def home(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('teacher-home')
        else:
            return redirect('student-home')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})
