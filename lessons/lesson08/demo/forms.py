from django import forms

from demo.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        # fields = ('first_name', 'last_name')
        exclude = ('created', 'updated')
        widgets = {
            'birth_of_date': forms.DateInput(attrs={'type': 'date'})
        }
