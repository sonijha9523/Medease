from .models import Medicines
from django.forms import ModelForm


class MedicinesForm(ModelForm):
	class Meta:
		model= Medicines
		fields = '__all__'


 