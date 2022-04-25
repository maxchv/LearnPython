from django.db import models


class StudentGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True)
    group = models.ForeignKey(StudentGroup, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
