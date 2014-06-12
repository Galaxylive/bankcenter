from django.contrib import admin

from .models import Atm


class AtmAdmin(admin.ModelAdmin):
    list_display = ("name_of_city", "name_of_bank")

admin.site.register(Atm, AtmAdmin)
