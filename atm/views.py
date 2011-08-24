# Create your views here.
from models import Atm
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import Http404
from utils import get_letters

def render(request, template, context):
    return render_to_response(template,context,context_instance = RequestContext(request))


def atms(request):
    letter=request.GET.get('letter','A')
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


