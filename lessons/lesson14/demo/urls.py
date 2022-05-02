from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import path, reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView

from demo.forms import PostForm
from demo.models import Post, Blog

app_name = 'demo'


class PostView(ListView):
    model = Post
    ordering = '-created'
    template_name = 'demo/index.html'
    context_object_name = 'posts'
    paginate_by = 10


class PersonalBlogPostView(ListView):
    context_object_name = 'posts'
    template_name = 'demo/index.html'

    def get_queryset(self):
        print('kwargs', self.kwargs)
        return Post.objects.filter(blog__slug=self.kwargs['name'])


class CreatePostView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    template_name = 'demo/post_create.html'
    fields = ('title', 'text')
    login_url = reverse_lazy('demo:login')

    def test_func(self):
        blog_slug = self.kwargs['name']
        user = self.request.user
        blog = Blog.objects.get(slug=blog_slug)
        if blog.author.user != user:
            return False
        return True

    def post(self, request, *args, **kwargs):
        blog_name = kwargs['name']
        form = PostForm(data=request.POST)
        post = form.save(commit=False)
        post.blog = Blog.objects.get(slug=blog_name)
        post.save()
        return redirect('demo:index')


class BlogLogin(LoginView):
    template_name = 'demo/login.html'
    success_url = reverse_lazy('demo:index')
    next_page = reverse_lazy('demo:index')


urlpatterns = [
    path('', PostView.as_view(), name='index'),
    path('login/', BlogLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('demo:index')), name='logout'),
    path('<slug:name>/', PersonalBlogPostView.as_view(), name='personal_blog'),
    path('<slug:name>/post/create', CreatePostView.as_view(), name='create_post'),
]
