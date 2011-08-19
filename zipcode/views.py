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

def detail(request):
   # return HttpResponse(request.GET['place'])
#  #   try:
    p = Zip_code.objects.filter(pin_code__iexact=request.GET['pincode'])
   # # except MultipleObjectsReturned:
    if p.count() > 0: 
        print "i am here"
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

        # r = Zip_code.objects.filter(post_office_name__iexact=request.GET['place'])
        # if r.count() > 0: return render(request, 'zipcode/detail.html', {'obj':r})
        # else:
        #     s = Zip_code.objects.filter(district_name__iexact=request.GET['place'])
        #     if s.count() > 0: return render(request, 'zipcode/detail.html', {'obj':s})
        #     else:
        #         t = Zip_code.objects.filter(city_name__iexact=request.GET['palce'])
        #         if t.count() > 0: return render(request, 'zipcode/detail.html', {'obj':t})
        #         else:
        #             u = Zip_code.objects.filter(state__iexact=request.GET['place'])
        #             if u.count() > 0: return render(request, 'zipcode/detail.html', {'obj':u})
        #             else: return render(request, 'zipcode/research.html', {})
                    
           
