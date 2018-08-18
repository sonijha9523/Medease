from django.contrib import admin

# Register your models here.
from .models import Medicines
from .models import Client
from .models import Med_Client_mapper
from .models import Med_Transaction

admin.site.register(Medicines)
admin.site.register(Client)
admin.site.register(Med_Client_mapper)
admin.site.register(Med_Transaction)
