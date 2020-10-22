from django import forms

from .models import ReturnedHomework

class ReturnedHomeworkForm(forms.ModelForm):
    class Meta:
        model = ReturnedHomework
        fields = ['hwfile',]