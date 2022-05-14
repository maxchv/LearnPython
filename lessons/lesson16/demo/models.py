from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description[:20]
