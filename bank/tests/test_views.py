

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from bank.models import Bank
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
