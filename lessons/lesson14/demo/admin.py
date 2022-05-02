from django.contrib import admin
from django.contrib.admin import register

from demo.models import Post, Blog, Author

admin.site.register(Post)
admin.site.register(Author)


@register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'author')
