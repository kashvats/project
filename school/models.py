from django.db import models

# Create your models here.
class student(models.Model):
    classe = models.CharField(max_length=3)
    roll = models.IntegerField(max_length=20)
    name = models.CharField(max_length=20)
    admissionid = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    mother = models.CharField(max_length=20)
    father = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    admissiondate = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class teacher(models.Model):
    tname = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    teacherid = models.CharField(max_length=25)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.tname





