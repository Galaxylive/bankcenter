from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import Http404
from django.db.models import Count

from models import Bank, Branch, Location, State
from utils import get_letters


def home(request):
    branches = Branch.objects.all()[:10]
    banks = Bank.objects.select_related().all().order_by(
        '-num_branches')[:20]
    locations = Location.objects.select_related().all().\
        order_by('-num_branches')[:20]
    return render(
        request, "bank/home.html",
        {'branch_list': branches, 'bank_list': banks,
            'location_list': locations})

def bank_branches(request, bank_slug):
    try:
        given_bank = Bank.objects.select_related().get(slug=bank_slug)
    except Bank.DoesNotExist:
        raise Http404
    branch_list = Branch.objects.select_related().filter(bank=given_bank)
    return render(request, "bank/bank_branches.html", {'bank':given_bank, 'branch_list':branch_list})
    
def branch_info(request, bank_slug, branch_slug, branch_ifsc):
    try:
        branch=Branch.objects.select_related().get(slug=branch_slug, bank__slug=bank_slug, ifsc=branch_ifsc)
        bank=Bank.objects.get(slug=bank_slug)
        bank.num_times_accessed += 1
        bank.save()
        loc=branch.location
        loc.num_times_accessed += 1
        loc.save()
        branch.save() #Each time this branch gets accessed, we call save() so that last_accessed field gets updated for this branch.
    except Branch.DoesNotExist, Bank.DoesNotExist:
        raise Http404
    return render_to_response("bank/branch_info.html",{'branch':branch},context_instance=RequestContext(request))
    
def city_branches(request, location_slug):
    branch_list = Branch.objects.select_related().filter(location__slug=location_slug)
    return render(request, 'bank/city_branches.html', {'location_slug':location_slug, 'branch_list':branch_list})
    
def state_branches(request, state_slug):
    state = State.objects.get(slug=state_slug)
    banks_list = Branch.objects.filter(location__state_fk=state).values('bank__bank_name').annotate(dcount=Count('bank__bank_name'))
    banks = [each['bank__bank_name'] for each in banks_list]
    return render(request, 'bank/state_branches.html', {'banks':banks, 'state':state})

def cities(request):
    letter = request.GET.get('letter', 'A')
    location_list = Location.objects.select_related().filter(
        city__startswith=letter)
    letters = get_letters()
    return render(
        request, 'bank/cities.html',
        {'location_list': location_list, 'letters': letters})
    
def banks(request):
    banks = Bank.objects.select_related().all()
    return render(request, "bank/banks.html", {'bank_list': banks})

def branch_with_ifsc(request, branch_ifsc):
    try:
        branch = Branch.objects.select_related().get(ifsc=branch_ifsc)
        branch.save()
    except Branch.DoesNotExist:
        raise Http404
    return render(request, 'bank/branch_info.html', {'branch': branch})

def branch_with_micr(request, branch_micr):
    try:
        branch = Branch.objects.select_related().get(micr=branch_micr)
        branch.save()
    except Branch.DoesNotExist:
        raise Http404
    return render(request, 'bank/branch_info.html', {'branch': branch})

def bank_city_branches(request, bank_slug, location_slug):
    try:
        branch_list = Branch.objects.select_related().filter(bank__slug=bank_slug, location__slug=location_slug)
        bank = Bank.objects.get(slug=bank_slug)
        bank.num_times_accessed += 1
        bank.save()
    except Branch.DoesNotExist:
        raise Http404
    return render(request, 'bank/bank_city_branches.html', {'branch_list':branch_list, 'bank': bank})
