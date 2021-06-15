from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','full_name','address','wallet',]
admin.site.register(Profile,ProfileAdmin)
