from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name=_("Category name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name=_("Post title"))
    content = models.TextField(verbose_name=_("Post content"))
    published_date = models.DateTimeField(auto_created=True, verbose_name=_("Post date published"))
    category = models.ForeignKey(Category, verbose_name=_("Category"))
    user = models.ForeignKey(User, verbose_name=_("Author"))
    image = models.URLField(default="http://placehold.it/900x300")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

