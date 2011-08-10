# Create your views here.
from models import Bank,Branch,Location,State
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from utils import get_letters
from django.http import Http404

def home(request):
    #bank_list=Bank.objects.select_related().all()
    branch_accessed_recently=Branch.objects.all()[:10]
    most_visited_banks=Bank.objects.select_related().all().order_by('-num_times_accessed')[:20]
    most_visited_locations=Location.objects.select_related().all().order_by('-num_times_accessed')[:20]
    return render(request,"bank/home.html",{'branch_list':branch_accessed_recently,'bank_list':most_visited_banks,'location_list':most_visited_locations})
    """bank_list=Bank.objects.select_related().all()
    paginator=Paginator(bank_list,20)
    pag=int(request.GET.get('page','1'))
    try:
        bank_list=paginator.page(pag)
    except PageNotAnInteger:
        bank_list=paginator.page(1)
    except EmptyPage:
        bank_list=paginator.page(paginator.num_pages)
    branch_accessed_recently=Branch.objects.all()[:10]
    return render(request,"bank/home.html",{'branch_list':branch_accessed_recently})"""
    
def bank_branches(request,bank_slug):
    #return HttpResponse("You are at {0}".format(bank_slug))
    given_bank=Bank.objects.select_related().get(slug=bank_slug)
    branch_list=Branch.objects.select_related().filter(bank=given_bank)
    #return HttpResponse("You are at {0}".format(bank_slug))
    return render(request,"bank/bank_branches.html",{'bank':given_bank,'branch_list':branch_list})
    
def branch_info(request,bank_slug,branch_slug):
    #return HttpResponse("")
    branch=Branch.objects.select_related().get(slug=branch_slug,bank__slug=bank_slug)
    bank=Bank.objects.get(slug=bank_slug)
    bank.num_times_accessed += 1
    bank.save()
    loc=branch.location
    loc.num_times_accessed += 1
    loc.save()
    branch.save() #Each time this branch gets accessed, we call save() so that last_accessed field gets updated for this branch.
    return render_to_response("bank/branch_info.html",{'branch':branch},context_instance=RequestContext(request))
    
def city_branches(request,location_slug):
    #return HttpResponse("You are at {0}".format(city_name))
    branch_list=Branch.objects.select_related().filter(location__slug=location_slug)
    #return HttpResponse("You are at {0}".format(city_name))
    return render(request,'bank/city_branches.html',{'location_slug':location_slug,'branch_list':branch_list})
    
def state_branches(request,state_slug):
    #return HttpResponse('You are at {0}'.format(state_slug)
    branch_list=Branch.objects.select_related().filter(location__state_fk__slug=state_slug)
    #return HttpResponse('You are at {0}'.format(state_slug))
    return render(request,'bank/state_branches.html',{'location_slug':state_slug,'branch_list':branch_list})
    
def cities(request):
    #return HttpResponse("Cities page")
    """location_list=Location.objects.select_related().all()
    return render(request,"bank/cities.html",{'location_list':location_list})"""
    
    letter=request.GET.get('letter','A')
    location_list=Location.objects.select_related().filter(city__startswith=letter)
    letters=get_letters()
    return render(request,'bank/cities.html',{'location_list':location_list,'letters':letters})
    """letter=request.GET.get('letter','A')
    location_list=Location.objects.select_related().filter(city__startswith=letter)
    letters=get_letters()
    paginator=Paginator(location_list,25)
    page=int(request.GET.get('page','1'))
    try:
        location_list=paginator.page(page)
    except PageNotAnInteger:
        location_list=paginator.page(1)
    except EmptyPage:
        location_list=paginator.page(paginator.num_pages)
    return render(request,'bank/cities.html',{'location_list':location_list,'letters':letters})"""
    
def banks(request):
    #return HttpResponse("You are at banks page")
    bank_list=Bank.objects.select_related().all()
    return render(request,"bank/banks.html",{'bank_list':bank_list})
    
def branch_with_ifsc(request,branch_ifsc):
    try:
        branch=Branch.objects.select_related().get(ifsc=branch_ifsc)
        branch.save()
    except Branch.DoesNotExist:
        raise Http404
    return render(request,'bank/branch_info.html',{'branch':branch})
    