# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Deleting model 'zipcode'
        db.delete_table('zipcode_zipcode')

        # Adding model 'Zip_code'
        db.create_table('zipcode_zip_code', (
            ('post_office_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('district_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pin_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('zipcode', ['Zip_code'])
    
    
    def backwards(self, orm):
        
        # Adding model 'zipcode'
        db.create_table('zipcode_zipcode', (
            ('post_office_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('district_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pin_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('zipcode', ['zipcode'])

        # Deleting model 'Zip_code'
        db.delete_table('zipcode_zip_code')
    
    
    models = {
        'zipcode.zip_code': {
            'Meta': {'object_name': 'Zip_code'},
            'city_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'district_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pin_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'post_office_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['zipcode']
