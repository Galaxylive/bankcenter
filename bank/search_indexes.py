from haystack import indexes

from .models import Branch


class BranchIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # branch_name = indexes.CharField(model_attr='branch_name')
    address = indexes.CharField(model_attr='address')

    def get_model(self):
        return Branch
