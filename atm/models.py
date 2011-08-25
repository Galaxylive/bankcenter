from django.db import models

# Create your models here.
class Atm(models.Model):
    name_of_city = models.CharField(max_length=100)
    name_of_bank = models.CharField(max_length=200)
    bank_slug = models.SlugField(max_length=100)
    city_slug = models.SlugField(max_length=100)
    address = models.CharField(max_length=500)


    def get_city_url(self):
        return "atms/city/%s" % self.city_slug
    
    def get_bank_url(self):
        return "atms/bank/%s" % self.bank_slug

    def get_detail_url(self):
        return "atms/%s/%s/%i" % (self.city_slug, self.bank_slug, self.id)

