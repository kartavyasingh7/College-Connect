from django.db import models

# Create your models here.

class Student(models.Model):
    enroll_no = models.BigIntegerField(primary_key=True)
    batch = models.CharField(max_length=2)
    year = models.CharField(max_length=3)

class FilesAdmin(models.Model):
	adminupload=models.FileField(upload_to='media')
	title=models.CharField(max_length=50)

class buySell(models.Model):
    enroll_no = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    img = models.ImageField(upload_to = 'pics')
    price = models.IntegerField()
    contact_no = models.IntegerField()
    desc = models.TextField(max_length=200)