from django.db import models

# Course
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
