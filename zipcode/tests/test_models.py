from django.test import TestCase

from zipcode.models import Zip_code


class ModelTests(TestCase):

    def setUp(self):
        pass

    def test_create_zipcodes(self):
        num = 3
        for i in range(num):
            Zip_code.objects.create(
                post_office_name="foo",
                pin_code="123456",
                district_name="test",
                city_name="city",
                state="abc",
                latitude=0,
                longitude=0
            )
        count = Zip_code.objects.count()
        self.assertEqual(count, num)
