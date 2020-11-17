from django.contrib import admin
from .models import *

@admin.register(Computer, IT, Mechanical, Electronics)
class ViewAdmin(admin.ModelAdmin):
	pass