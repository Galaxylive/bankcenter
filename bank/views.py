# Create your views here.
from models import Bank,Branch,Location,State
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext

def home(request):
    bank_list=Bank.objects.select_related().all()
    branch_accessed_recently=Branch.objects.all()[:10]
    return render(request,"bank/home.html",{'branch_list':branch_accessed_recently})
    
def bank_branches(request,bank_slug):
    #return HttpResponse("You are at {0}".format(bank_slug))
    given_bank=Bank.objects.select_related().get(slug=bank_slug)
    branch_list=Branch.objects.select_related().filter(bank=given_bank)
    #return HttpResponse("You are at {0}".format(bank_slug))
    return render(request,"bank/bank_branches.html",{'bank':given_bank,'branch_list':branch_list})
    
def branch_info(request,bank_slug,branch_slug):
    #return HttpResponse("")
    branch=Branch.objects.select_related().get(slug=branch_slug,bank__slug=bank_slug)
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