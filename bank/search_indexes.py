from haystack.indexes import *
from haystack import site
from bank.models import Location, Bank, Branch

class BranchIndex(SearchIndex):
    branch_name = CharField(document=True, use_template=True)
    address = CharField(model_attr='address')

site.register(Branch, BranchIndex)
