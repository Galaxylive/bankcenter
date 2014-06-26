from django.http import Http404
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, ListView, DetailView

from .models import Bank, Branch, Location, State
from .utils import get_letters


class HomeView(TemplateView):
    template_name = "bank/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        branches = Branch.objects.all()[:10]
        banks = Bank.objects.order_by('-num_branches')[:21]
        locations = Location.objects.order_by('-num_branches')[:21]
        context.update({'branch_list': branches, 'bank_list': banks,
                       'location_list': locations})
        return context


class BanksView(ListView):
    template_name = "bank/banks.html"
    queryset = Bank.objects.all()
    context_object_name = 'bank_list'


class CitiesView(ListView):
    template_name = 'bank/cities.html'
    context_object_name = 'location_list'

    def get_context_data(self, **kwargs):
        context = super(CitiesView, self).get_context_data(**kwargs)
        context['letters'] = get_letters()
        return context

    def get_queryset(self):
        letter = self.request.GET.get('letter', 'A')
        location_list = Location.objects.filter(
            city__startswith=letter)
        return location_list


class BranchBaseView(DetailView):
    template_name = 'bank/branch_info.html'
    context_object_name = 'branch'

    def get_obj(self, key, value):
        try:
            branch = Branch.objects.select_related().get(**{key: value})
            bank = branch.bank
            bank.num_times_accessed += 1
            bank.save()
            loc = branch.location
            loc.num_times_accessed += 1
            loc.save()
            branch.save()
        except Branch.DoesNotExist:
            raise Http404
        return branch


class BranchIfscView(BranchBaseView):

    def get_object(self, queryset=None):
        branch_ifsc = self.kwargs.get('branch_ifsc', '')
        return self.get_obj('ifsc', branch_ifsc)


class BranchMicrView(BranchBaseView):

    def get_object(self, queryset=None):
        branch_micr = self.kwargs.get('branch_micr', '')
        return self.get_obj('micr', branch_micr)


class CityBranchesView(ListView):
    template_name = 'bank/city_branches.html'
    context_object_name = 'branch_list'

    def get_queryset(self):
        location_slug = self.kwargs.get('location_slug', '')
        branch_list = Branch.objects.select_related().filter(
            location__slug=location_slug
        )
        return branch_list

    def get_context_data(self, **kwargs):
        context = super(CityBranchesView, self).get_context_data(**kwargs)
        context['location_slug'] = self.kwargs.get('location_slug', '')
        return context


class StateBranchesView(TemplateView):
    template_name = 'bank/state_branches.html'

    def get_context_data(self, **kwargs):
        state_slug = self.kwargs.get('state_slug', '')
        state = State.objects.get(slug=state_slug)
        banks = Branch.objects.filter(location__state_fk=state).values(
            'bank__bank_name',
            'bank__slug'
        ).annotate(dcount=Count('bank__bank_name'))
        context = super(StateBranchesView, self).get_context_data(**kwargs)
        context['banks'] = banks
        context['state'] = state
        return context


class BankStateBranchesView(TemplateView):
    template_name = 'bank/bank_state_branches.html'

    def get_context_data(self, **kwargs):
        state_slug = self.kwargs.get('state_slug', '')
        bank_slug = self.kwargs.get('bank_slug', '')
        context = super(BankStateBranchesView, self).get_context_data(**kwargs)
        try:
            branch_list = Branch.objects.select_related().filter(
                bank__slug=bank_slug,
                location__state_fk__slug=state_slug
            )
            bank = Bank.objects.get(slug=bank_slug)
            bank.num_times_accessed += 1
            bank.save()
        except Bank.DoesNotExist:
            raise Http404
        context.update({'branch_list': branch_list, 'bank': bank})
        return context


class BankBranchesView(TemplateView):
    template_name = "bank/bank_branches.html"

    def get(self, request, *args, **kwargs):
        self.context_data = {}
        bank_slug = kwargs.get('bank_slug', '')
        try:
            given_bank = Bank.objects.get(slug=bank_slug)
        except Bank.DoesNotExist:
            raise Http404

        branch_list = Branch.objects.select_related().filter(bank=given_bank)

        paginator = Paginator(branch_list, 20)
        page = int(request.GET.get('page', 1))

        try:
            branch_list = paginator.page(page)
        except PageNotAnInteger:
            branch_list = paginator.page(1)
        except EmptyPage:
            branch_list = paginator.page(paginator.num_pages)

        max_range = page + 3
        if max_range > paginator.num_pages:
            max_range = paginator.num_pages + 1
        pages = range(page - 3, max_range)
        pages = [pagenum for pagenum in pages if pagenum > 0]
        self.context_data['branch_list'] = branch_list
        self.context_data['bank'] = given_bank
        self.context_data['pages'] = pages
        return super(BankBranchesView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BankBranchesView, self).get_context_data(**kwargs)
        context.update(self.context_data)
        return context


class BankCityBranchesView(ListView):
    template_name = 'bank/bank_city_branches.html'

    def get_queryset(self):
        bank_slug = self.kwargs.get('bank_slug', '')
        location_slug = self.kwargs.get('location_slug', '')
        try:
            branch_list = Branch.objects.select_related().filter(
                bank__slug=bank_slug,
                location__slug=location_slug
            )
            self.bank = Bank.objects.get(slug=bank_slug)
            self.bank.num_times_accessed += 1
            self.bank.save()
        except Bank.DoesNotExist:
            raise Http404
        return branch_list

    def get_context_data(self, **kwargs):
        context = super(BankCityBranchesView, self).get_context_data(**kwargs)
        context['bank'] = self.bank
        return context


class BranchInfoView(DetailView):
    template_name = "bank/branch_info.html"
    context_object_name = 'branch'

    def get_object(self, queryset=None):
        branch_slug = self.kwargs.get('branch_slug', '')
        bank_slug = self.kwargs.get('bank_slug', '')
        branch_ifsc = self.kwargs.get('branch_ifsc', '')
        try:
            branch = Branch.objects.select_related().get(
                slug=branch_slug,
                bank__slug=bank_slug,
                ifsc=branch_ifsc
            )
            bank = Bank.objects.get(slug=bank_slug)
            bank.num_times_accessed += 1
            bank.save()
            loc = branch.location
            loc.num_times_accessed += 1
            loc.save()
            # Each time this branch gets accessed, we call save() so that
            # last_accessed field gets updated for this branch.
            branch.save()
        except Branch.DoesNotExist, Bank.DoesNotExist:
            raise Http404
        return branch
