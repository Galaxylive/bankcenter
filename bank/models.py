from django.db import models
from django.template.defaultfilters import slugify

import datetime


class State(models.Model):
    state = models.CharField(max_length=200)
    slug = models.SlugField(null=False, max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.state)
        super(State, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.state


class Location(models.Model):
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    slug = models.SlugField(null=True, max_length=200)
    state_fk = models.ForeignKey(State, null=True)
    num_times_accessed = models.IntegerField(default=0)
    num_branches = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.city)
        super(Location, self).save(*args, **kwargs)

    def __unicode__(self):
        return "{0}, {1}".format(self.city, self.state)

    def __eq__(self, other):
        if (self.city == other.city and
                self.district == other.district and self.state == other.state):
            return True
        else:
            return False

    def __hash__(self):
        return len(self.city) + len(self.district) + len(self.state)

    class Meta:
        ordering = ['city', 'district']


class Bank(models.Model):
    bank_name = models.CharField(max_length=300)
    slug = models.SlugField(null=True, max_length=300)
    num_times_accessed = models.IntegerField(default=0)
    num_branches = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.bank_name)
        super(Bank, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.bank_name


class Branch(models.Model):
    branch_name = models.CharField(max_length=300)
    ifsc = models.CharField(max_length=11)
    micr = models.CharField(max_length=9, blank=True, null=True)
    address = models.CharField(max_length=300)
    contact = models.CharField(max_length=300)
    bank = models.ForeignKey(Bank)
    location = models.ForeignKey(Location)
    slug = models.SlugField(max_length=200)
    last_accessed = models.DateTimeField(
        auto_now=True, default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.branch_name)
        super(Branch, self).save(*args, **kwargs)

    def __unicode__(self):
        return "{0}, {1}, {2}".\
            format(self.bank, self.branch_name, self.location)

    class Meta:
        verbose_name_plural = 'Branches'
        ordering = ['-last_accessed']
