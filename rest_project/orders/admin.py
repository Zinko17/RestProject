from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','profile','quantity','date_created','status','total_sum']
    readonly_fields = ['total_sum','profile','date_created']
# Register your models here.
