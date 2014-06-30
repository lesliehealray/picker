# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Song.librettist_lname'
        db.delete_column(u'rep_song', 'librettist_lname')

        # Deleting field 'Song.librettist_fname'
        db.delete_column(u'rep_song', 'librettist_fname')

        # Adding field 'Song.librettist_first_name'
        db.add_column(u'rep_song', 'librettist_first_name',
                      self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Song.librettist_last_name'
        db.add_column(u'rep_song', 'librettist_last_name',
                      self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Song.librettist_lname'
        raise RuntimeError("Cannot reverse this migration. 'Song.librettist_lname' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Song.librettist_lname'
        db.add_column(u'rep_song', 'librettist_lname',
                      self.gf('django.db.models.fields.CharField')(max_length=75),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Song.librettist_fname'
        raise RuntimeError("Cannot reverse this migration. 'Song.librettist_fname' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Song.librettist_fname'
        db.add_column(u'rep_song', 'librettist_fname',
                      self.gf('django.db.models.fields.CharField')(max_length=75),
                      keep_default=False)

        # Deleting field 'Song.librettist_first_name'
        db.delete_column(u'rep_song', 'librettist_first_name')

        # Deleting field 'Song.librettist_last_name'
        db.delete_column(u'rep_song', 'librettist_last_name')


    models = {
        u'rep.artist': {
            'Meta': {'object_name': 'Artist'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'rep.composer': {
            'Meta': {'object_name': 'Composer'},
            'birth_year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'death_year': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
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
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rep.Program']"}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rep.Song']"})
        },
        u'rep.song': {
            'Meta': {'object_name': 'Song'},
            'composer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rep.Composer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'librettist_first_name': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'librettist_last_name': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['rep']