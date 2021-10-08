from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class student(models.Model):
    classe = models.CharField(max_length=3)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    roll = models.IntegerField(max_length=20)
    name = models.CharField(max_length=20)
    admissionid = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    mother = models.CharField(max_length=20)
    father = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    admissiondate = models.DateField(default=timezone.now())

    def __str__(self):
        return self.name

class teacher(models.Model):
    tname = models.CharField(max_length=20)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    teacherid = models.CharField(max_length=25)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.tname





