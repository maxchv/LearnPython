from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(max_length=16, min_length=3)
    password = forms.CharField(max_length=16, min_length=5)

