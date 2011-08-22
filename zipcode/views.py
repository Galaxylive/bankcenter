# Create your views here.
from models import Zip_code
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import Http404
from django.db.models import Q

obj = Zip_code.objects.all()
def render(request, template, context):
    return render_to_response(template,context,context_instance = RequestContext(request))

def pincode(request):
    return render(request, 'zipcode/formpage.html', {})
    #
def city(request, city_id=None):
    p = Zip_code.objects.filter(city_name__iexact = city_id)
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
    return render(request, 'zipcode/city_detail.html', {'obj' : contents})
    
    

def detail(request):
    p = Zip_code.objects.filter(pin_code__iexact=request.GET['pincode'])
    if p.count() > 0: 
        return render(request, 'zipcode/detail.html', {'obj':p})
    else:
        p = Zip_code.objects.filter(\
            Q(post_office_name__iexact=request.GET['place']) |\
            Q(district_name__iexact=request.GET['place']) |\
            Q(city_name__iexact=request.GET['place']) |\
            Q(state__iexact=request.GET['place'])\
            )             
        if p.count() > 0: return render(request, 'zipcode/detail.html', {'obj':p})
        else: return render(request, 'zipcode/research.html', {})

    
