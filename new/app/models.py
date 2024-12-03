from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.IntegerField()
    name = models.TextField(max_length=30)
    age = models.IntegerField()