from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Location(models.Model):
    city=models.CharField(max_length=200)
    district=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    
    def __unicode__(self):
        return "{0}, {1}".format(self.city,self.state)
        
class Bank(models.Model):
    bank_name=models.CharField(max_length=300)
    
    def __unicode__(self):
        return self.bank_name
    
class Branch(models.Model):
    branch_name=models.CharField(max_length=300)
    ifsc=models.CharField(max_length=11)
    micr=models.CharField(max_length=9,blank=True,null=True) #We will set invalid micr codes to None which will be stored as null in database
    address=models.CharField(max_length=300)
    contact=models.CharField(max_length=300)
    bank=models.ForeignKey(Bank)
    location=models.ForeignKey(Location)
    slug=models.SlugField(unique=True)
    
    def save(self,**kwargs):
        if not self.slug:
            self.slug=slugify(self.bank,self.branch_name)
        super(Branch,self).save(**kwargs)
    
    def __unicode__(self):
        return "{0}, {1}, {2}".format(self.bank,self.branch_name,self.location)
        
    class Meta:
        verbose_name_plural='Branches'
        

    
