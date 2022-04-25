from django import forms

from demo.models import Student, StudentGroup


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class StudentGroupForm(forms.ModelForm):

    class Meta:
        model = StudentGroup
        fields = '__all__'
