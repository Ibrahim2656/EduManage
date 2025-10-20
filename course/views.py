from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import ManualCourseForm


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


def course_add(request):
    form = ManualCourseForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        Course.objects.create(code=data['code'], name=data['name'])
        return redirect('course_list')
    return render(request, 'course_form_manual.html', {'form': form})


def course_edit(request, code):
    course = get_object_or_404(Course, code=code)
    if request.method == 'POST':
        form = ManualCourseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            course.code = data['code']
            course.name = data['name']
            course.save()
            return redirect('course_list')
    else:
        form = ManualCourseForm(initial={'code': course.code, 'name': course.name})
    return render(request, 'course_form_manual.html', {'form': form})


def course_delete(request, code):
    course = get_object_or_404(Course, code=code)
    course.delete()
    return redirect('course_list')
