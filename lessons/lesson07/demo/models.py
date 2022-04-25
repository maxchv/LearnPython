from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    date_of_birth = models.DateField(null=True)
