# forms.py
from django import forms
from .models import Student, Course


class StudentForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Student
        fields = '__all__'
