# Create your views here.
from models import Bank,Branch,Location
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext

def home(request):
    bank_list=Bank.objects.all()
    return render(request,"bank/home.html")
    
def bank_branches(request,bank_slug):
    #return HttpResponse("You are at {0}".format(bank_slug))
    given_bank=Bank.objects.get(slug=bank_slug)
    branch_list=Branch.objects.filter(bank=given_bank)
    #return HttpResponse("You are at {0}".format(bank_slug))
    return render(request,"bank/bank_branches.html",{'bank':given_bank,'branch_list':branch_list})
    
def branch_info(request,bank_slug,branch_slug):
    #return HttpResponse("")
    branch=Branch.objects.get(slug=branch_slug,bank__slug=bank_slug)
    return render_to_response("bank/branch_info.html",{'branch':branch},context_instance=RequestContext(request))