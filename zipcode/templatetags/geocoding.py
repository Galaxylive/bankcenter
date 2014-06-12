import urllib
import json

from django import template
from django.utils.safestring import mark_safe

#from zipcode.models import Ziop_code
from pprint import pprint

register = template.Library()
#ref : http://code.google.com/apis/maps/documentation/geocoding/#GeocodingRequests

url = "http://maps.googleapis.com/maps/api/geocode/json?address="
post_office = "A G'S Office Staff "
city = "Hyderabad "
state = "Andhra Pradesh "
address = post_office + city + state
url += address + "&sensor=true"

raw = urllib.urlopen(url)
json_object = json.load(raw)
#pprint(json_object)
lat = json_object['results'][0]['geometry']['location']['lat']
lng = json_object['results'][0]['geometry']['location']['lng']
print lat, lng


@register.filter
def get_lat_lng(, autoescape=None):
    ret_str = ""
    for i in recipe.ingredients_present.all():
        name = i.name.lower()
        api_url = get_img_url(name)
        ret_str += "<img src='" + api_url + "' alt='" + name +  "'  />\n"
    return mark_safe(ret_str)
