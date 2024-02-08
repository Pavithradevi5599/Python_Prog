from django.db import models

# Create your models here.
class Data(models.Model):
    Name=models.CharField(max_length=20)
    Mobile=models.CharField(max_length=20)