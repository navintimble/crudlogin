from django.db import models


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)


class Employee(models.Model):
    eid = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=70)
    edate = models.CharField(max_length=70)
    eposition = models.CharField(max_length=70)
    esallery = models.CharField(max_length=70)
    eleft = models.CharField(max_length=70)


class Investment(models.Model):
    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    invid = models.AutoField(primary_key=True)
    invdate = models.CharField(max_length=70)
    invpayd = models.CharField(max_length=70)
    invrs = models.CharField(max_length=70)

