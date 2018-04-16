from django.test import TestCase

from atm.models import Atm


class ModelTests(TestCase):

    def setUp(self):
        pass

    def test_create_atms(self):
        num = 3
        for i in range(num):
            Atm.objects.create(
                name_of_city="foo",
                name_of_bank="bar",
                address="address"
            )
        count = Atm.objects.count()
        self.assertEqual(count, num)
