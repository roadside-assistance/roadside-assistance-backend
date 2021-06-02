from django.contrib import admin

# Register your models here.
from humanResources.models.citizen import Citizen
from humanResources.models.stateExpert import StateExpert

admin.site.register(Citizen)
admin.site.register(StateExpert)
