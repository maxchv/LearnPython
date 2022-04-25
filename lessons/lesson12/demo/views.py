from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import LoginForm


def login_view(request):
    form = LoginForm()
    if request.method == 'GET':
        return render(request, 'demo/login.html', {'form': form})
    elif request.method == 'POST':
        try:
            user = authenticate(username=request.POST.get('login'),
                                password=request.POST.get('password'))
            login(request, user)
        except Exception as e:
            print(e)
            return render(request, 'demo/login.html', {'form': LoginForm(data=request.POST)})
        return redirect('demo:index')
