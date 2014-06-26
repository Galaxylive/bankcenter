from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Atm
from .utils import get_letters


class AtmBaseView(TemplateView):
    context_data = {}

    def get_context_data(self, **kwargs):
        context = super(AtmBaseView, self).get_context_data(**kwargs)
        context.update(self.context_data)
        return context


class AtmView(AtmBaseView):
    template_name = 'atm/index.html'

    def get(self, request, *args, **kwargs):
        self.context_data = {}
        letter = request.GET.get('letter', None)
        if not letter:
            obj = Atm.objects.order_by("bank_slug")
        else:
            obj = Atm.objects.filter(
                name_of_bank__startswith=letter)
        paginator = Paginator(obj, 20)  # show 20 recipes per page
        page = int(request.GET.get('page', 1))
        try:
            contents = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contents = paginator.page(1)
        except EmptyPage:
          # If page is out of range, deliver last page of results.
            contents = paginator.page(paginator.num_pages)
        letters = get_letters()
        max_range = page + 3
        if max_range > paginator.num_pages:
            max_range = paginator.num_pages + 1
        pages = range(page - 3, max_range)
        pages = [pagenum for pagenum in pages if pagenum > 0]
        self.context_data.update({
            'atms': contents,
            'letters': letters,
            'current_letter': letter,
            'pages': pages
        })
        return super(AtmView, self).get(request, *args, **kwargs)


class CityView(AtmBaseView):
    template_name = 'atm/atms_by_city.html'

    def get(self, request, *args, **kwargs):
        city_id = kwargs.get('city_id', None)
        self.context_data = {}
        p = Atm.objects.filter(city_slug__iexact=city_id)
        if p.count() == 0:
            raise Http404
        paginator = Paginator(p, 10)  # show 10 atms per page
        page = int(request.GET.get('page', 1))
        try:
            contents = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contents = paginator.page(1)
        except EmptyPage:
          # If page is out of range, deliver last page of results.
            contents = paginator.page(paginator.num_pages)
        max_range = page + 3
        if max_range > paginator.num_pages:
            max_range = paginator.num_pages + 1
        pages = range(page - 3, max_range)
        pages = [pagenum for pagenum in pages if pagenum > 0]
        self.context_data.update({
            'cities': contents,
            'name': city_id,
            'pages': pages
        })
        return super(CityView, self).get(request, *args, **kwargs)


class BankView(AtmBaseView):
    template_name = 'atm/atms_by_bank.html'

    def get(self, request, *args, **kwargs):
        self.context_data = {}
        bank_id = kwargs.get('bank_id', None)
        p = Atm.objects.filter(bank_slug=bank_id)
        if p.count() == 0:
            raise Http404
        paginator = Paginator(p, 10)  # show 10 atms per page
        page = int(request.GET.get('page', 1))
        try:
            contents = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contents = paginator.page(1)
        except EmptyPage:
          # If page is out of range, deliver last page of results.
            contents = paginator.page(paginator.num_pages)
        max_range = page + 3
        if max_range > paginator.num_pages:
            max_range = paginator.num_pages + 1
        pages = range(page - 3, max_range)
        pages = [pagenum for pagenum in pages if pagenum > 0]
        self.context_data.update({
            'banks': contents,
            'name': bank_id,
            'pages': pages
        })
        return super(BankView, self).get(request, *args, **kwargs)


class AtmDetailView(DetailView):
    template_name = 'atm/atm_detail.html'
    context_object_name = 'atm'

    def get_object(self, queryset=None):
        city_id = self.kwargs.get('city_id', None)
        bank_id = self.kwargs.get('bank_id', None)
        detail_id = self.kwargs.get('detail_id', None)
        atm = get_object_or_404(Atm, city_slug=city_id,
                                bank_slug=bank_id, pk=detail_id)
        return atm



