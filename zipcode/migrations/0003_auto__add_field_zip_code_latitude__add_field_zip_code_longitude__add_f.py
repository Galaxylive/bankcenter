# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Zip_code.latitude'
        db.add_column(u'zipcode_zip_code', 'latitude',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Zip_code.longitude'
        db.add_column(u'zipcode_zip_code', 'longitude',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Zip_code.city_slug'
        db.add_column(u'zipcode_zip_code', 'city_slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Zip_code.latitude'
        db.delete_column(u'zipcode_zip_code', 'latitude')

        # Deleting field 'Zip_code.longitude'
        db.delete_column(u'zipcode_zip_code', 'longitude')

        # Deleting field 'Zip_code.city_slug'
        db.delete_column(u'zipcode_zip_code', 'city_slug')


    models = {
        u'zipcode.zip_code': {
            'Meta': {'object_name': 'Zip_code'},
            'city_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city_slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'district_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'pin_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'post_office_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['zipcode']