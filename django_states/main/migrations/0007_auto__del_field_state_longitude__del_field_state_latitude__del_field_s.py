# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'State.longitude'
        db.delete_column(u'main_state', 'longitude')

        # Deleting field 'State.latitude'
        db.delete_column(u'main_state', 'latitude')

        # Deleting field 'State.population'
        db.delete_column(u'main_state', 'population')


    def backwards(self, orm):
        # Adding field 'State.longitude'
        db.add_column(u'main_state', 'longitude',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'State.latitude'
        db.add_column(u'main_state', 'latitude',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'State.population'
        db.add_column(u'main_state', 'population',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


    models = {
        u'main.state': {
            'Meta': {'object_name': 'State'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'main.statecapital': {
            'Meta': {'object_name': 'StateCapital'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'population': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['main']