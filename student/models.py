from django.db import models
from course.models import Course
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    image = models.ImageField(upload_to='student/images/',null=True,blank=True)
    date_of_birth = models.DateField(default='2000-01-01')
    
    courses = models.ManyToManyField(Course,blank=True)
    
    
    
    def __str__(self):
        return self.name