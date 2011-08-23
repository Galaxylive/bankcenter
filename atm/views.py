# Create your views here.
from models import Atm
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import Http404

def render(request, template, context):
    return render_to_response(template,context,context_instance = RequestContext(request))

def atms(request):
    return HttpResponse("Hello from atms")
#return render(request, '', {})
