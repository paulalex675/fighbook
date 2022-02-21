from django.db import models

# Create your models here.

class Styles(models.Model):
    StyleId = models.AutoField(primary_key=True)
    StyleName = models.CharField(max_length=100)

class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserUserName = models.CharField(max_length=100)
    UserFirstName = models.CharField(max_length=100)
    UserLastName = models.CharField(max_length=100)
    DateOfBirth = models.DateField()
    PhotoFileName = models.CharField(max_length=100)