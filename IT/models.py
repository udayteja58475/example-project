from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)
    regnumber=models.IntegerField()
    age=models.IntegerField()
    department=models.CharField(max_length=20)
    def __str__(self):
        return self.name