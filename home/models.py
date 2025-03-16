from django.db import models


# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    email = models.EmailField()
    date_born = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    freelance = models.BooleanField()
    address_web = models.CharField(max_length=50)
    degree_of_education = models.CharField(max_length=500)
    profession = models.CharField(max_length=500)