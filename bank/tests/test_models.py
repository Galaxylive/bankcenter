from django.test import TestCase

from bank.models import State, Location, Bank, Branch


class ModelTests(TestCase):

    def setUp(self):
        pass

    def test_create_states(self):
        num = 3
        for i in range(num):
            create_state()
        count = State.objects.count()
        self.assertEqual(count, num)
        state = State.objects.latest('id')
        self.assertEqual(state.slug, "foo-bar")

    def test_create_location(self):
        create_location()
        count = Location.objects.count()
        self.assertEqual(count, 1)

    def test_create_banks(self):
        num = 3
        for i in range(num):
            create_bank()
        count = Bank.objects.count()
        self.assertEqual(count, num)

    def test_create_branches(self):
        num = 3
        for i in range(num):
            create_branch()
        count = Branch.objects.count()
        self.assertEqual(count, num)


def create_state():
    return State.objects.create(
        state="foo bar",
    )


def create_location():
    state = create_state()
    location = Location.objects.create(
        city="test",
        district="abc",
        state=state.state,
        state_fk=state
    )
    return location


def create_bank():
    return Bank.objects.create(
        bank_name="test"
    )


def create_branch():
    bank = create_bank()
    location = create_location()
    branch = Branch.objects.create(
        branch_name='test',
        ifsc='12345678911',
        micr='ABCDE1234',
        address='address',
        contact='1234567890',
        bank=bank,
        location=location
    )
    return branch
