# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'StateCapital.state'
        db.delete_column(u'main_statecapital', 'state_id')

        # Adding M2M table for field state on 'StateCapital'
        m2m_table_name = db.shorten_name(u'main_statecapital_state')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('statecapital', models.ForeignKey(orm[u'main.statecapital'], null=False)),
            ('state', models.ForeignKey(orm[u'main.state'], null=False))
        ))
        db.create_unique(m2m_table_name, ['statecapital_id', 'state_id'])


    def backwards(self, orm):
        # Adding field 'StateCapital.state'
        db.add_column(u'main_statecapital', 'state',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['main.State']),
                      keep_default=False)

        # Removing M2M table for field state on 'StateCapital'
        db.delete_table(db.shorten_name(u'main_statecapital_state'))


    models = {
        u'main.state': {
            'Meta': {'object_name': 'State'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'main.statecapital': {
            'Meta': {'object_name': 'StateCapital'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.State']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['main']