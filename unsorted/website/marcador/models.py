from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['name']

    def __str__(self):
        return self.name


class PublicBookmarkManager(models.Model):
    def get_queryset(self):
        qs = super(PublicBookmarkManager, self).get_queryset()
        return qs.filter(is_public=True)


class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    owner = models.ForeignKey(User, verbose_name='owner', related_name='bookmarks')
    tags = models.ManyToManyField(Tag, blank=True)

    objects = models.Manager()
    public = PublicBookmarkManager()

    class Meta:
        verbose_name = 'bookmark'
        verbose_name_plural = 'bookmarks'
        ordering = ['-date_created']

    def __str__(self):
        return "{} ({})".format(self.title, self.url)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(Bookmark, self).save(*args, **kwargs)

