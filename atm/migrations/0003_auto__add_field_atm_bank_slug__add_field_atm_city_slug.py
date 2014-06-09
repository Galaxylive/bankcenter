# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Atm.bank_slug'
        db.add_column(u'atm_atm', 'bank_slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Atm.city_slug'
        db.add_column(u'atm_atm', 'city_slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Atm.bank_slug'
        db.delete_column(u'atm_atm', 'bank_slug')

        # Deleting field 'Atm.city_slug'
        db.delete_column(u'atm_atm', 'city_slug')


    models = {
        u'atm.atm': {
            'Meta': {'object_name': 'Atm'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'bank_slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'city_slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_of_bank': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_of_city': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['atm']