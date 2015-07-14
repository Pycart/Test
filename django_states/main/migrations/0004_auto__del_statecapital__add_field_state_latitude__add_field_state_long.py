# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'StateCapital'
        db.delete_table(u'main_statecapital')

        # Adding field 'State.latitude'
        db.add_column(u'main_state', 'latitude',
                      self.gf('django.db.models.fields.FloatField')(default=1),
                      keep_default=False)

        # Adding field 'State.longitude'
        db.add_column(u'main_state', 'longitude',
                      self.gf('django.db.models.fields.FloatField')(default=1),
                      keep_default=False)

        # Adding field 'State.population'
        db.add_column(u'main_state', 'population',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'StateCapital'
        db.create_table(u'main_statecapital', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.State'])),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('population', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'main', ['StateCapital'])

        # Deleting field 'State.latitude'
        db.delete_column(u'main_state', 'latitude')

        # Deleting field 'State.longitude'
        db.delete_column(u'main_state', 'longitude')

        # Deleting field 'State.population'
        db.delete_column(u'main_state', 'population')


    models = {
        u'main.state': {
            'Meta': {'object_name': 'State'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'population': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['main']