from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


class Zip_code(models.Model):
    post_office_name = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    district_name = models.CharField(max_length=50)
    city_name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    city_slug = models.SlugField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.city_slug:
            self.city_slug = slugify(self.city_name)
        super(Zip_code, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.post_office_name

    def get_absolute_url(self):
        return reverse("city", args=[self.city_slug])
