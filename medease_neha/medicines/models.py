# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.forms import ModelForm
from decimal import *
from string import *
from number import *
from django.forms import DecimalField
from decimal import Decimal
# Create your models here.

class Medicines(models.Model):
	'''mid = models.AutoField()'''
	mname = models.CharField(max_length=200,unique=True,primary_key=True)
	med_type = models.CharField(max_length=50)
	
	def __str__(self):
		return self.mname


class Client(models.Model):
	'''cid = models.AutoField()'''
	cname = models.CharField(max_length=200,unique=True)
	address = models.CharField(max_length=200)
	email = models.EmailField(max_length=254)
	phone_regex = RegexValidator(regex=r'^\d{9,10}$', message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=11, blank=False,primary_key=True) # validators should be a list

	def __str__(self):
		return self.cname

	def getClientName(self):
		return self.cname

class Med_Client_mapper(models.Model):
	mname_mapper = models.ManyToManyField(Medicines)
	client_contact_mapper = models.ForeignKey(Client,on_delete="models.CASCADE")
	selling_price_per_box = models.DecimalField(decimal_places=3,max_digits=10)
	no_of_box_sell = models.DecimalField(decimal_places=3,max_digits=10)

	def __str__(self):
		return self.generate_mapper_name()

	def generate_mapper_name(self):
		mapper_name = str(self.mname_mapper)+'____'+str(self.client_contact_mapper)
		return mapper_name


class Med_Transaction(models.Model):
	mname_mapper = models.ForeignKey(Medicines,on_delete="models.CASCADE")
	company_cost =  models.DecimalField(decimal_places=3,max_digits=10)
	lending_cost =  models.DecimalField(decimal_places=3,max_digits=10)
	opening_unit =  models.PositiveIntegerField()
	recieving_unit = models.PositiveIntegerField()
	closing_unit = models.PositiveIntegerField()
	
	def cal_selling_unit(openingunit,recievingunit,closingunit):
		sellingunit = number(openingunit) +recievingunit-closingunit
		return sellingunit

	selling_unit =cal_selling_unit(opening_unit,recieving_unit,closing_unit)
