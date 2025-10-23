from django.contrib import admin

# Register your models here.
from .models import (District, Suguan, Credential)

# @admin.register(LCC)

class District_Admin(admin.ModelAdmin):
   list_display = ["id","dcode", "lcode","name","office", "contact", "phone", "region","r"]
   ordering = ['id']
   search_fields = ["lcode__startswith","name__startswith", "contact__startswith", "region__startswith"]

class Suguan_Admin(admin.ModelAdmin):
   list_display = ["week", "name", "date", "day", "locale"]
   ordering = ['-date']
   search_fields = ["week__startswith", "date__startswith","day__startswith", "locale__startswith"]

class Credential_Admin(admin.ModelAdmin):
   list_display = ["lvm", "lcode", "computer", "user", "password", "bios", "note"]
   ordering = ['lcode']
   search_fields = ["lcode__startswith", "user__startswith"]

admin.site.register(District, District_Admin)
admin.site.register(Suguan, Suguan_Admin)
admin.site.register(Credential, Credential_Admin)
