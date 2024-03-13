from django.contrib import admin
from . models import *

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'rent')
    list_filter = ('location',)
    search_fields = ['name']

class EmailAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'message')
    search_fields = ['name']

admin.site.register(Location)
admin.site.register(CarDealer)
admin.site.register(Car, CarAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Email)
