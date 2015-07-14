# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'StateCapital.longitude'
        db.alter_column(u'main_statecapital', 'longitude', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'StateCapital.latitude'
        db.alter_column(u'main_statecapital', 'latitude', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'StateCapital.population'
        db.alter_column(u'main_statecapital', 'population', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'StateCapital.longitude'
        db.alter_column(u'main_statecapital', 'longitude', self.gf('django.db.models.fields.FloatField')(default=1))

        # Changing field 'StateCapital.latitude'
        db.alter_column(u'main_statecapital', 'latitude', self.gf('django.db.models.fields.FloatField')(default=1))

        # Changing field 'StateCapital.population'
        db.alter_column(u'main_statecapital', 'population', self.gf('django.db.models.fields.IntegerField')(default=1))

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
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.State']", 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['main']