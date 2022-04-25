from django.db import models


class Student(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50, null=False, blank=False)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50, null=False, blank=False)
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
