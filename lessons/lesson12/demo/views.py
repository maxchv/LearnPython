from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect

from .forms import LoginForm, PostForm


def login_view(request):
    form = LoginForm()
    print(request.user)
    if request.method == 'GET':
        return render(request, 'demo/login.html', {'form': form})
    elif request.method == 'POST':
        try:
            user = authenticate(username=request.POST.get('login'),
                                password=request.POST.get('password'))
            if user:
                login(request, user)
        except Exception as e:
            print(e)
            return render(request, 'demo/login.html', {'form': LoginForm(data=request.POST)})
        next = request.GET.get('next', 'demo:index')
        return redirect(next)


def logout_view(request):
    logout(request)
    return redirect("demo:index")


@login_required
def create_post(request):
    # if request.user.is_authenticated:
    context = {'form': PostForm()}
    return render(request, 'demo/create_post.html', context)


# else:
#     return redirect('demo:login')


# @user_passes_test(lambda u: u.has_perm('demo.delete_post'), login_url='/login/')
@permission_required('demo.delete_post', raise_exception=True)
def delete_post(request):
    return render(request, 'demo/delete_post.html')


class OnlyForAuthenticatedUsersView(PermissionRequiredMixin, TemplateView):
    permission_required = 'demo.delete_post'
    template_name = 'demo/secured.html'
    login_url = reverse_lazy('demo:login')
    extra_context = {'title': 'Only for authenticated users'}
