from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import Http404
from django.db.models import Q

from models import Zip_code

obj = Zip_code.objects.all()
def render(request, template, context):
    return render_to_response(template, context, context_instance=RequestContext(request))

def pincode(request):
    return render(request, 'zipcode/formpage.html', {})
    
def city(request, city_id=None):
    p = Zip_code.objects.filter(city_slug__iexact=city_id)
    if p.count() == 0:
        raise Http404
    paginator = Paginator(p,5)#show 20 recipes per page
    page = request.GET.get('page', 1)
    try:
        contents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contents = paginator.page(1)
    except EmptyPage:
      #If page is out of range, deliver last page of results.
        contents = paginator.page(paginator.num_pages)
    return render(request, 'zipcode/city_detail.html', {'cities' : contents})
    
def detail(request):
    pincode = request.GET.get('pincode', '')
    place = request.GET.get('place', '')
    p = Zip_code.objects.filter(pin_code=pincode)
    if p.count() > 0: 
        return render(request, 'zipcode/detail.html', {'cities':p})
    else:
        p = Zip_code.objects.filter(\
            Q(post_office_name__iexact=place) |\
            Q(district_name__iexact=place) |\
            Q(city_name__iexact=place) |\
            Q(state__iexact=place)\
            )             
    if p.count() > 0:
        return render(request, 'zipcode/detail.html', {'cities':p})
    else:
        return render(request, 'zipcode/research.html', {})
