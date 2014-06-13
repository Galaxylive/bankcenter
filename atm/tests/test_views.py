"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from atm.models import Atm


class AtmTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_first_page(self):
        response = self.c.get(reverse("atm_home"))
        self.assertEqual(response.status_code, 200)

    def test_pagination(self):
        no = 100
        for each in range(no):
            Atm.objects.create(
                name_of_city="test",
                name_of_bank="foo",
                address="address"
            )
        self.assertEqual(Atm.objects.count(), 100)
        response = self.c.get("{0}?page={1}".format(reverse("atm_home"), 2))
        self.assertEqual(response.status_code, 200)

    def test_CityView(self):
        Atm.objects.create(
            name_of_city="test",
            name_of_bank="foo",
            address="address"
        )
        self.assertEqual(Atm.objects.count(), 1)
        response = self.c.get(reverse('atms_in_city', args=['test']))
        self.assertEqual(response.status_code, 200)
        response = self.c.get(reverse('atms_in_city', args=['invalid']))
        self.assertEqual(response.status_code, 404)

    def test_BankView(self):
        Atm.objects.create(
            name_of_city="test",
            name_of_bank="foo",
            address="address"
        )
        self.assertEqual(Atm.objects.count(), 1)
        response = self.c.get(reverse('atms_for_bank', args=['foo']))
        self.assertEqual(response.status_code, 200)
        response = self.c.get(reverse('atms_for_bank', args=['invalid']))
        self.assertEqual(response.status_code, 404)

    def test_DetailView(self):
        Atm.objects.create(
            name_of_city="test",
            name_of_bank="foo",
            address="address"
        )
        self.assertEqual(Atm.objects.count(), 1)
        atm = Atm.objects.all()[0]
        response = self.c.get(reverse('atm_detail', args=['test', 'foo', atm.id]))
        self.assertEqual(response.status_code, 200)
        response = self.c.get(reverse('atm_detail', args=['test', 'foo', 5]))
        self.assertEqual(response.status_code, 404)
