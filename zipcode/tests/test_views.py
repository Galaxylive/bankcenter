

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from zipcode.models import Zip_code


class ZipcodeTestCase(TestCase):

    def setUp(self):
        self.c = Client()
        self.pincode = Zip_code.objects.create(
            post_office_name="foo",
            pin_code="123456",
            district_name="test",
            city_name="city",
            state="abc",
            latitude=0,
            longitude=0
        )

    def test_PincodeView(self):
        response = self.c.get(reverse("pincode_home"))
        self.assertEqual(response.status_code, 200)

    def test_PincodeDetailView(self):
        response = self.c.get("{0}?pincode={1}".format(reverse("detail"), '123456'))
        result = response.context['cities']
        self.assertEqual(result[0].pin_code, '123456')

    def test_CityView(self):
        response = self.c.get(reverse('city', args=['city']))
        self.assertEqual(response.status_code, 200)
        response = self.c.get(reverse('city', args=['invalid']))
        self.assertEqual(response.status_code, 404)

    def test_PinDetailView(self):
        response = self.c.get(reverse('pincode_pin_detail', args=['123456']))
        result = response.context['places']
        self.assertEqual(len(result), 1)
        response = self.c.get(reverse('pincode_pin_detail', args=['123']))
        result = response.context['places']
        self.assertEqual(len(result), 0)
