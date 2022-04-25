from django import forms
from django.core import validators


class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=30)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
