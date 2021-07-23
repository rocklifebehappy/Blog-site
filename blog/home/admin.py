from django.contrib import admin
from .models import World, InformationTechnology, RemoteDevelopment, Agriculture, Bioinformatics, \
	EnvironmentalTechnology

# Register your models here.
"""
This admin.py is used to register the model in the admin site.
Check in documentation for more information.
"""

admin.site.register(World)
admin.site.register(InformationTechnology)
admin.site.register(RemoteDevelopment)
admin.site.register(Agriculture)
admin.site.register(Bioinformatics)
admin.site.register(EnvironmentalTechnology)