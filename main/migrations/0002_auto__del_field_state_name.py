# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'State.name'
        db.delete_column(u'main_state', 'name')


    def backwards(self, orm):
        # Adding field 'State.name'
        db.add_column(u'main_state', 'name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100, unique=True),
                      keep_default=False)


    models = {
        u'main.state': {
            'Meta': {'object_name': 'State'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'capital': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'population': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['main']