# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Location.num_branches'
        db.add_column('bank_location', 'num_branches', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Location.num_branches'
        db.delete_column('bank_location', 'num_branches')


    models = {
        'bank.bank': {
            'Meta': {'object_name': 'Bank'},
            'bank_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_branches': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_times_accessed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '300', 'null': 'True', 'db_index': 'True'})
        },
        'bank.branch': {
            'Meta': {'ordering': "['-last_accessed']", 'object_name': 'Branch'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'bank': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bank.Bank']"}),
            'branch_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ifsc': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'last_accessed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bank.Location']"}),
            'micr': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'db_index': 'True'})
        },
        'bank.location': {
            'Meta': {'ordering': "['city', 'district']", 'object_name': 'Location'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_branches': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_times_accessed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'null': 'True', 'db_index': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'state_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bank.State']", 'null': 'True'})
        },
        'bank.state': {
            'Meta': {'object_name': 'State'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'db_index': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['bank']
