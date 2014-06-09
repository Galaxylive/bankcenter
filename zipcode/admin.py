from .models import Zip_code
from django.contrib import admin


class ZipCodeAdmin(admin.ModelAdmin):
    list_display = ("pin_code", "post_office_name")

admin.site.register(Zip_code, ZipCodeAdmin)
