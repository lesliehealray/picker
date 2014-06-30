# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Song.composer' to match new field type.
        db.rename_column(u'rep_song', 'composer', 'composer_id')
        # Changing field 'Song.composer'
        db.alter_column(u'rep_song', 'composer_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rep.Composer']))
        # Adding index on 'Song', fields ['composer']
        db.create_index(u'rep_song', ['composer_id'])


    def backwards(self, orm):
        # Removing index on 'Song', fields ['composer']
        db.delete_index(u'rep_song', ['composer_id'])


        # Renaming column for 'Song.composer' to match new field type.
        db.rename_column(u'rep_song', 'composer_id', 'composer')
        # Changing field 'Song.composer'
        db.alter_column(u'rep_song', 'composer', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'rep.composer': {
            'Meta': {'object_name': 'Composer'},
            'b_year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'd_year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'f_name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'l_name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'rep.program': {
            'Meta': {'object_name': 'Program'},
            'create_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'perf_date': ('django.db.models.fields.DateField', [], {}),
            'songs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['rep.Song']", 'through': u"orm['rep.ProgramSong']", 'symmetrical': 'False'})
        },
        u'rep.programsong': {
            'Meta': {'object_name': 'ProgramSong'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rep.Program']"}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rep.Song']"})
        },
        u'rep.song': {
            'Meta': {'object_name': 'Song'},
            'composer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rep.Composer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'librettist_fname': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'librettist_lname': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['rep']