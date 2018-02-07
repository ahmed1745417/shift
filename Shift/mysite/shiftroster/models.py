from django.db import models

# Create your models here.

class Emp(models.Model):
    name=models.CharField(max_length=200)
    id=models.CharField(primary_key=True,max_length=100)
    weekoff1=models.IntegerField()
    weekoff2=models.IntegerField()
    team=models.IntegerField()

class Roster(models.Model):
    shift_date=models.DateField()
    name=models.CharField(max_length=200)
    eid=models.CharField(max_length=100)
    shift=models.CharField(max_length=200)
