from django.db import models


class Person(models.Model):
    gender = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('UNKNOWN', 'Unknown'),
    )
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=7, choices=gender, default='UNKNOWN')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'People'
