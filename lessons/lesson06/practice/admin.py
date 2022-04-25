from django.contrib import admin

from practice.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'gender')
