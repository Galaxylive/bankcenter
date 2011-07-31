# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Location'
        db.create_table('bank_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bank', ['Location'])

        # Adding model 'Bank'
        db.create_table('bank_bank', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bank_name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('bank', ['Bank'])

        # Adding model 'Branch'
        db.create_table('bank_branch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('branch_name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('ifsc', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('micr', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('bank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bank.Bank'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bank.Location'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, db_index=True)),
            ('last_accessed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
        ))
        db.send_create_signal('bank', ['Branch'])


    def backwards(self, orm):
        
        # Deleting model 'Location'
        db.delete_table('bank_location')

        # Deleting model 'Bank'
        db.delete_table('bank_bank')

        # Deleting model 'Branch'
        db.delete_table('bank_branch')


    models = {
        'bank.bank': {
            'Meta': {'object_name': 'Bank'},
            'bank_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
            'Meta': {'object_name': 'Location'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['bank']
