from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import Http404

from atm.models import Atm
from atm.utils import get_letters


def detail(request, city_id, bank_id, detail_id=None):
    atm = get_object_or_404(Atm, city_slug=city_id, 
                            bank_slug=bank_id, pk = detail_id)
    return render(request, 'atm/atm_detail.html', {'atm': atm})

def bank(request, bank_id=None):
    p = Atm.objects.filter(bank_slug=bank_id)
    if p.count() == 0:
        raise Http404
    paginator = Paginator(p, 10)#show 10 atms per page
    page = int(request.GET.get('page', 1))
    try:
        contents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contents = paginator.page(1)
    except EmptyPage:
      #If page is out of range, deliver last page of results.
        contents = paginator.page(paginator.num_pages)
    max_range = page+3
    if max_range > paginator.num_pages:
        max_range = paginator.num_pages+1
    pages = range(page-3, max_range)
    pages = [pagenum for pagenum in pages if pagenum>0]
    return render(request, 'atm/atms_by_bank.html', {'banks' : contents, 'name':bank_id, 'pages': pages})


def city(request, city_id=None):
    p = Atm.objects.filter(city_slug__iexact=city_id)
    if p.count() == 0:
        raise Http404
    paginator = Paginator(p, 10)#show 10 atms per page
    page = int(request.GET.get('page', 1))
    try:
        contents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contents = paginator.page(1)
    except EmptyPage:
      #If page is out of range, deliver last page of results.
        contents = paginator.page(paginator.num_pages)
	letters=get_letters()
    max_range = page+3
    if max_range > paginator.num_pages:
        max_range = paginator.num_pages+1
    pages = range(page-3, max_range)
    pages = [pagenum for pagenum in pages if pagenum>0]
    return render(request, 'atm/atms_by_city.html', {'cities' : contents, 'name':city_id, 'pages': pages})


def atms(request):
    letter=request.GET.get('letter', '')
    if not letter:
        obj = Atm.objects.all().order_by("bank_slug")
    else:
        obj = Atm.objects.select_related().filter(name_of_bank__startswith=letter)
    paginator = Paginator(obj, 20)#show 20 recipes per page
    page = int(request.GET.get('page', 1))
    try:
        contents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contents = paginator.page(1)
    except EmptyPage:
      #If page is out of range, deliver last page of results.
        contents = paginator.page(paginator.num_pages)
    letters=get_letters()
    max_range = page+3
    if max_range > paginator.num_pages:
        max_range = paginator.num_pages+1
    pages = range(page-3, max_range)
    pages = [pagenum for pagenum in pages if pagenum>0]
    return render(request, 'atm/index.html', {'atms':contents, 'letters':letters, 'current_letter':letter,'pages': pages})
