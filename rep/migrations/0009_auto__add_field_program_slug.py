# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Program.slug'
        db.add_column(u'rep_program', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='added slugfield', unique=True, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Program.slug'
        db.delete_column(u'rep_program', 'slug')


    models = {
        u'rep.artist': {
            'Meta': {'object_name': 'Artist'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'})
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
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
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
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['rep']