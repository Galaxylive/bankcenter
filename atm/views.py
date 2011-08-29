from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import Http404

from atm.models import Atm
from atm.utils import get_letters

def render(request, template, context):
    return render_to_response(template,context,context_instance = RequestContext(request))


def detail(request, city_id, bank_id, detail_id=None):
    atm = Atm.objects.get(pk = detail_id)
    return render(request, 'atm/atm_detail.html', {'atm': atm})

def bank(request, bank_id=None):
    p = Atm.objects.filter(bank_slug = bank_id)
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
    return render(request, 'atm/atms_by_bank.html', {'obj' : contents, 'name':bank_id})


def city(request, city_id=None):
    p = Atm.objects.filter(city_slug__iexact = city_id)
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
    return render(request, 'atm/atms_by_city.html', {'obj' : contents, 'name':city_id})


def atms(request):
    letter=request.GET.get('letter','')
    if not letter:
        obj = Atm.objects.all().order_by("?")
    else:
        obj = Atm.objects.select_related().filter(name_of_bank__startswith=letter)
    paginator = Paginator(obj,10)#show 20 recipes per page
    page = request.GET.get('page', 1)
    try:
        contents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contents = paginator.page(1)
    except EmptyPage:
      #If page is out of range, deliver last page of results.
        contents = paginator.page(paginator.num_pages)
    letters=get_letters()
    return render(request, 'atm/index.html', {'obj':contents, 'letters':letters, 'current_letter':letter})


