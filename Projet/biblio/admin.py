from django.contrib import admin
from .models import Livre,Emprunt

# Register your models here.
admin.site.register(Livre)
admin.site.register(Emprunt)