from django.db import models

# Create your models here.
class Emp(models.Model):
    Empid=models.CharField(max_length=30,default=True,blank=True)
    Empname=models.CharField(max_length=30,default=True,blank=True)
    Empsal=models.IntegerField(default=True,blank=True)
    Empexp=models.IntegerField(default=True,blank=True)
    Empadd=models.CharField(max_length=30,default=True,blank=True)

