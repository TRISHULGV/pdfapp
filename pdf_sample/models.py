from statistics import mode
from django.db import models

# Create your models here.

class Pdf(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='images')

def __str__(self):
    return self.title

