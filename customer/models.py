from django.db import models
from django.forms import ModelForm
import datetime

# Create your models here.

class UserEntity(models.Model):
	entity_type_id = models.IntegerField(max_length=2, default='0')
	group_id = models.IntegerField(max_length=2, default='0')
	fname = models.CharField(max_length=30, default='')
	lname = models.CharField(max_length=30, default='')
	sex = models.CharField(max_length=1, default='')
	date_of_birth = models.CharField(max_length=10, default='')
	address_1 = models.CharField(max_length=255, default='')
	address_2 = models.CharField(max_length=30, default='')
	city = models.CharField(max_length=255, default='')
	region = models.CharField(max_length=255, default='')
	country = models.CharField(max_length=255, default='')
	zipcode = models.CharField(max_length=255, default='')
	email = models.EmailField(max_length=255, default='')
	username = models.CharField(max_length=30, default='')
	password = models.CharField(max_length=30, default='')
	phone = models.CharField(max_length=20, default='')
	image = models.CharField(max_length=255, default='')
	create_time = models.DateTimeField(default=datetime.datetime.now())
	update_time = models.DateTimeField(default=datetime.datetime.now())
	is_active = models.BooleanField(default='1')
	recent_ip = models.CharField(max_length=15, default='')
	
			