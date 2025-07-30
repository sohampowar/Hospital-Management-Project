from django.db import models

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    contact=models.IntegerField()
    consulting=models.CharField(max_length=100)

