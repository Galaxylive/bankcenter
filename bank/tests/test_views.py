

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from bank.models import Bank, Branch
from .test_models import (create_state, create_location,
                          create_bank, create_branch)


class BankTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_first_page(self):
        response = self.c.get(reverse("bank_home"))
        self.assertEqual(response.status_code, 200)

    def test_BanksView(self):
        num = 10
        for i in range(num):
            create_bank()
        response = self.c.get(reverse("bank_banks"))
        banks = response.context['bank_list']
        self.assertEqual(len(banks), 10)

    def test_CitiesView(self):
        num = 10
        for i in range(num):
            create_location()
        response = self.c.get("{0}?letter={1}".format(
            reverse("bank_cities"), 't'))
        locations = response.context['location_list']
        self.assertEqual(len(locations), 10)

    def test_BranchIfscView(self):
        ifsc = 'RNSB0000001'
        create_branch()
        response = self.c.get(
            reverse('bank_branch_with_ifsc', args=[ifsc]))
        branch = response.context['branch']
        self.assertEqual(branch.ifsc, ifsc)

    def test_BranchMicrView(self):
        micr = '360217002'
        create_branch()
        response = self.c.get(
            reverse('bank_branch_with_micr', args=[micr]))
        branch = response.context['branch']
        self.assertEqual(branch.micr, micr)

    def test_CityBranchesView(self):
        location_slug = 'test'
        create_branch()
        response = self.c.get(
            reverse('bank_city_branches', args=[location_slug]))
        branches = response.context['branch_list']
        self.assertEqual(len(branches), 1)

    def test_StateBranchesView(self):
        state_slug = 'foo-bar'
        create_branch()
        response = self.c.get(
            reverse('bank_state_branches', args=[state_slug]))
        banks = response.context['banks']
        state = response.context['state']
        self.assertEqual(len(banks), 1)
        self.assertEqual(state.slug, state_slug)

    def test_BankStateBranchesView(self):
        state_slug = 'foo-bar'
        bank_slug = 'test'
        create_branch()
        response = self.c.get(
            reverse('bank_bank_state_branches', args=[state_slug, bank_slug]))
        branches = response.context['branch_list']
        bank = response.context['bank']
        self.assertEqual(len(branches), 1)
        self.assertEqual(bank.slug, bank_slug)

    def test_BankBranchesView(self):
        bank_slug = 'test'
        create_branch()
        response = self.c.get(
            reverse('bank_bank_branches', args=[bank_slug]))
        branches = response.context['branch_list']
        bank = response.context['bank']
        self.assertEqual(len(branches), 1)
        self.assertEqual(bank.slug, bank_slug)

    def test_BankCityBranchesView(self):
        location_slug = 'test'
        bank_slug = 'test'
        create_branch()
        response = self.c.get(
            reverse('bank_bank_city_branches', args=[bank_slug, location_slug]))
        branches = response.context['branch_list']
        bank = response.context['bank']
        self.assertEqual(len(branches), 1)
        self.assertEqual(bank.slug, bank_slug)

    def test_BranchInfoView(self):
        bank_slug = 'test'
        branch_slug = 'test'
        ifsc = 'RNSB0000001'
        create_branch()
        response = self.c.get(
            reverse('bank_branch_info', args=[bank_slug, branch_slug, ifsc]))
        self.assertEqual(response.status_code, 200)
