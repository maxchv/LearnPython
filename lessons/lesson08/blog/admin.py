from django.contrib import admin

from .models import Post, Tag, Category, Comment


@admin.register(Post, Tag, Category, Comment)
class BlogAdmin(admin.ModelAdmin):
    pass


