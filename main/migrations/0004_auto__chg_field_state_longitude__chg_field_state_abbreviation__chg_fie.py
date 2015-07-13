# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'State.longitude'
        db.alter_column(u'main_state', 'longitude', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'State.abbreviation'
        db.alter_column(u'main_state', 'abbreviation', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'State.capital'
        db.alter_column(u'main_state', 'capital', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'State.latitude'
        db.alter_column(u'main_state', 'latitude', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'State.population'
        db.alter_column(u'main_state', 'population', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'State.longitude'
        db.alter_column(u'main_state', 'longitude', self.gf('django.db.models.fields.FloatField')(default=1))

        # Changing field 'State.abbreviation'
        db.alter_column(u'main_state', 'abbreviation', self.gf('django.db.models.fields.CharField')(default=1, max_length=2))

        # Changing field 'State.capital'
        db.alter_column(u'main_state', 'capital', self.gf('django.db.models.fields.CharField')(default=1, max_length=100))

        # Changing field 'State.latitude'
        db.alter_column(u'main_state', 'latitude', self.gf('django.db.models.fields.FloatField')(default=1))

        # Changing field 'State.population'
        db.alter_column(u'main_state', 'population', self.gf('django.db.models.fields.IntegerField')(default=1))

    models = {
        u'main.state': {
            'Meta': {'object_name': 'State'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'capital': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']