from django import forms

from demo.models import Post


class LoginForm(forms.Form):
    login = forms.CharField(max_length=16, min_length=3)
    password = forms.CharField(max_length=16, min_length=5)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text', )


