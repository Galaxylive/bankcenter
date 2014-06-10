from atm.models import Atm
from django.contrib import admin


class AtmAdmin(admin.ModelAdmin):
    list_display = ("name_of_city", "name_of_bank")

admin.site.register(Atm, AtmAdmin)
