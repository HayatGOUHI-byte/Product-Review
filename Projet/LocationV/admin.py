from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(Voiture)
admin.site.register(Permis_Conduite)
admin.site.register(Client)
admin.site.register(Statut)
admin.site.register(Reservation)
admin.site.register(Paiement)