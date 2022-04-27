from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_student =models.BooleanField(default=False)
class Student(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='student')
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email= models.EmailField(max_length=254)
    contact_no =models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Book(models.Model):
    name= models.CharField(max_length=250)
    type=models.CharField(max_length=250)
    description= models.TextField()
    def __str__(self):
        return self.name


