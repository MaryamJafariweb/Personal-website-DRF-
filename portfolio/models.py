from django.db import models


# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=70)
    producer = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    skills = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolios/%Y/%m/%d')
    body = models.TextField()
