from django.db import models

# Create your models here.

class Trainers(models.Model):
    deptno=models.IntegerField(primary_key=True)
    tname=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)


    def __str__(self):
        return self.tname



class Students(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    deptno=models.ForeignKey(Trainers,on_delete=models.CASCADE)


    def __str__(self):
        return self.sname
