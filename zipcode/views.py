from django.http import Http404
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from models import Zip_code


class PincodeView(TemplateView):
    template_name = 'zipcode/formpage.html'


class PincodeDetailView(TemplateView):
    template_name = 'zipcode/formpage.html'

    def get(self, request, *args, **kwargs):
        self.context_data = {}
        self.result = False
        pincode = request.GET.get('pincode', '')
        place = request.GET.get('place', '')
        p = Zip_code.objects.filter(pin_code=pincode)
        if not p.count():
            p = Zip_code.objects.filter(
                Q(post_office_name__iexact=place) |
                Q(district_name__iexact=place) |
                Q(city_name__iexact=place) |
                Q(state__iexact=place)
            )
        if p.count():
            self.template_name = 'zipcode/detail.html'
            self.context_data['cities'] = p
            self.result = True
        return super(PincodeDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PincodeDetailView, self).get_context_data(**kwargs)
        context.update(self.context_data)
        if not self.result:
            context["no_result"] = True
        return context


class CityView(TemplateView):
    template_name = 'zipcode/city_detail.html'

    def get(self, request, *args, **kwargs):
        self.context_data = {}
        city_slug = kwargs.get('city_slug', '')
        p = Zip_code.objects.filter(city_slug__iexact=city_slug)
        if not p.count():
            raise Http404
        paginator = Paginator(p, 10)  # show 20 recipes per page
        page = request.GET.get('page', 1)
        try:
            contents = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contents = paginator.page(1)
        except EmptyPage:
            #If page is out of range, deliver last page of results.
            contents = paginator.page(paginator.num_pages)
        self.context_data['cities'] = contents
        return super(CityView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CityView, self).get_context_data(**kwargs)
        context.update(self.context_data)
        return context


class PinDetailView(ListView):
    template_name = 'zipcode/pin_detail.html'
    context_object_name = 'places'

    def get_queryset(self):
        pin = self.kwargs.get('pin', '')
        places = Zip_code.objects.filter(pin_code=pin)
        return places


# obj = Zip_code.objects.all()
# def render(request, template, context):
#     return render_to_response(template, context, context_instance=RequestContext(request))


# def detail(request):
#     pincode = request.GET.get('pincode', '')
#     place = request.GET.get('place', '')
#     p = Zip_code.objects.filter(pin_code=pincode)
#     if p.count():
#         return render(request, 'zipcode/detail.html', {'cities':p})
#     else:
#         p = Zip_code.objects.filter(\
#             Q(post_office_name__iexact=place) |\
#             Q(district_name__iexact=place) |\
#             Q(city_name__iexact=place) |\
#             Q(state__iexact=place)\
#             )
#     if p.count():
#         return render(request, 'zipcode/detail.html', {'cities':p})
#     else:
#         return render(request, 'zipcode/formpage.html', {"no_result": True})


# def pincode(request):
#     return render(request, 'zipcode/formpage.html', {})

# def city(request, city_slug=None):
#     p = Zip_code.objects.filter(city_slug__iexact=city_slug)
#     if not p.count():
#         raise Http404
#     paginator = Paginator(p, 10)#show 20 recipes per page
#     page = request.GET.get('page', 1)
#     try:
#         contents = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         contents = paginator.page(1)
#     except EmptyPage:
#       #If page is out of range, deliver last page of results.
#         contents = paginator.page(paginator.num_pages)
#     return render(request, 'zipcode/city_detail.html', {'cities' : contents})

# def detail(request):
#     pincode = request.GET.get('pincode', '')
#     place = request.GET.get('place', '')
#     p = Zip_code.objects.filter(pin_code=pincode)
#     if p.count():
#         return render(request, 'zipcode/detail.html', {'cities':p})
#     else:
#         p = Zip_code.objects.filter(\
#             Q(post_office_name__iexact=place) |\
#             Q(district_name__iexact=place) |\
#             Q(city_name__iexact=place) |\
#             Q(state__iexact=place)\
#             )
#     if p.count():
#         return render(request, 'zipcode/detail.html', {'cities':p})
#     else:
#         return render(request, 'zipcode/formpage.html', {"no_result": True})

# def pin_detail(request, pin):
#     places = Zip_code.objects.filter(pin_code=pin)
#     return render(request, 'zipcode/pin_detail.html', {'places': places})
