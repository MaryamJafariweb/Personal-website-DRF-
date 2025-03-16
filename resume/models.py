from django.db import models

# Create your models here.

class EducationExperiences(models.Model):
    title = models.CharField(max_length=50)
    times = models.CharField(max_length=20)
    body = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.title}-{self.body[:20]}'


class Skills(models.Model):
    title = models.CharField(max_length=50)
    percent = models.CharField(max_length=20)
    body = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.title}-{self.body[:20]}'

