from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=255)
	phone = models.CharField(max_length=13)
	email = models.EmailField(max_length=255,unique=True)
	password = models.CharField(max_length=20)

	def __str__(self):
		return self.username

# from django.contrib.auth.models import User

class UsrRegModel(models.Model):
    root_user = models.OneToOneField(User,on_delete=models.CASCADE)
    usr_name = models.CharField(max_length=500)
    usr_email = models.CharField(max_length=500 ,null=True,blank=True)
    usr_email_password = models.CharField(max_length=500 ,null=True,blank=True)
    usr_ph_otp = models.PositiveIntegerField(max_length=6 ,null=True,blank=True)
    usr_email_otp = models.PositiveIntegerField(max_length=6 ,null=True,blank=True)