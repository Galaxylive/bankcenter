from django.core.urlresolvers import reverse
from django.db import models


class Zip_code(models.Model):
    post_office_name=models.CharField(max_length=50)
    pin_code=models.CharField(max_length=10)
    district_name=models.CharField(max_length=50)
    city_name=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField() 
    city_slug = models.SlugField(max_length=100)
    
    def __unicode__(self):
        return self.post_office_name

    def get_absolute_url(self):
        return reverse("city", args=[self.city_slug])
