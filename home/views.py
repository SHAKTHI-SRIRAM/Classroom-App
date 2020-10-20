from django.shortcuts import render, redirect

from .forms import UserRegisterForm


def home(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('teacher-home')
        else:
            return redirect('student-home')
    else:
        return render(request, 'main-home.html')


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
