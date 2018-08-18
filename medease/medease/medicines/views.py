from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import CreateView
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
#from medicines.models import Medicines
from .forms import MedicinesForm
#from .serializers import MedicinesSerializer
from medicines.models import Med_Transaction,Med_Client_mapper,Client,Medicines
from django.urls import reverse, reverse_lazy, resolve 
# Create your views here.
'''class MedicinesCreateView(CreateView):
	def get(self, request, *args, **kwargs):
		#return HttpResponse('Hello, World!')
		model = Medicines
		form_class = MedicinesForm
		success_url = reverse_lazy('medicines')
		templates ='medicines.html'
		return render(request,templates,context)
	form_class = MedicinesForm
    #login_url = '/login/'
	template_name = 'medicines.html'
    #success_url = "/restaurants/"

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(MedicinesCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(MedicinesCreateView, self).get_context_data(*args, **kwargs)
		context['mname'] = 'Add Restaurant'
		return context'''

	
'''class MedicinesList(APIView):
	docstring for ClassName
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		
	def get(self,request):
		med= Medicines.objects.all()
		serializer=MedicinesSerializer(med,many=True)
		return Response(serializer.data)

	def post(self):
		pass'''
def MedicinesList(request):
	Meds=Medicines.objects.all()
	MedTrans=Med_Transaction.objects.all()
	MedResult=Medicines.objects.get(mname='dcold')

	
	#context={'Meds':Meds,'MedTrans':MedTrans}
	return render(request,'medicines.html',{'MedResult':MedResult})