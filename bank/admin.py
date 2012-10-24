from django.contrib import admin
from django import forms

from models import Branch, Bank, Location, State

"""ifsc code of Branch should be of fixed length i.e of 11 characters.
    This can not be done with models.CharField, so we create
    a ModelForm named BranchForm which lets us choose max_length
    as well as min_length"""


class BranchForm(forms.ModelForm):
    #This makes ifsc of fixed length of 11 characters.
    ifsc = forms.CharField(max_length=11, min_length=11)

    class Meta:
        model = Branch


class BranchAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('branch_name',)}
    form = BranchForm
    search_fields = ['bank__bank_name']


admin.site.register(Branch, BranchAdmin)
admin.site.register(Bank)
admin.site.register(Location)
admin.site.register(State)
