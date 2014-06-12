from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


class Atm(models.Model):
    name_of_city = models.CharField(max_length=100)
    name_of_bank = models.CharField(max_length=200)
    bank_slug = models.SlugField(max_length=100)
    city_slug = models.SlugField(max_length=100)
    address = models.CharField(max_length=500)

    def save(self, *args, **kwargs):
        if not self.bank_slug:
            self.bank_slug = slugify(self.name_of_bank)
        if not self.city_slug:
            self.city_slug = slugify(self.name_of_city)
        super(Atm, self).save(*args, **kwargs)

    def get_city_url(self):
        return reverse("atms_in_city", args=[self.city_slug])

    def get_bank_url(self):
        return reverse("atms_for_bank", args=[self.bank_slug])

    def get_detail_url(self):
        url = reverse("atm_detail",
                      args=[self.city_slug, self.bank_slug, self.pk])
        return url
