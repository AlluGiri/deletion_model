from django.db import models

# Create your models here.

class country(models.Model):
    cname=models.CharField(max_length=50,primary_key=True)
    ccode=models.BigIntegerField()
