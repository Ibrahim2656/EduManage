from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
