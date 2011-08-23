from django.db import models

# Create your models here.
class Atm(models.Model):
    name_of_city = models.CharField(max_length=100)
    name_of_bank = models.CharField(max_length=200)
    address = models.CharField(max_length=500)



