from django import forms

from .models import ReturnedHomework

class ReturnHomeworkForm(forms.ModelForm):
    class Meta:
        model = ReturnedHomework
        fields = ('hwfile',)