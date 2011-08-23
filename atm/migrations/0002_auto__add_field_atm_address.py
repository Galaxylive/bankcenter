# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'Atm.address'
        db.add_column('atm_atm', 'address', self.gf('django.db.models.fields.CharField')(default=datetime.date(2011, 8, 23), max_length=500), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting field 'Atm.address'
        db.delete_column('atm_atm', 'address')
    
    
    models = {
        'atm.atm': {
            'Meta': {'object_name': 'Atm'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_of_bank': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_of_city': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['atm']
