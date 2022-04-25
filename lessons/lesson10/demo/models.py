from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    genders = (('MALE', 'Male'), ('FEMALE', 'Female'), ('UNKNOWN', 'Unknown'))
    gender = models.CharField(max_length=7, choices=genders)
    birth_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
