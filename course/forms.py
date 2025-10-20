from django import forms

class ManualCourseForm(forms.Form):
    code = forms.CharField(max_length=20, label='Course Code')
    name = forms.CharField(max_length=100, label='Course Name')
