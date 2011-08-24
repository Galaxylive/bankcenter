# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Atm'
        db.create_table('atm_atm', (
            ('name_of_bank', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_of_city', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('atm', ['Atm'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Atm'
        db.delete_table('atm_atm')
    
    
    models = {
        'atm.atm': {
            'Meta': {'object_name': 'Atm'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_of_bank': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_of_city': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['atm']
