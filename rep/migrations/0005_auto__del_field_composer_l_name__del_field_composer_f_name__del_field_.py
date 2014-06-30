# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Composer.l_name'
        db.delete_column(u'rep_composer', 'l_name')

        # Deleting field 'Composer.f_name'
        db.delete_column(u'rep_composer', 'f_name')

        # Deleting field 'Composer.b_year'
        db.delete_column(u'rep_composer', 'b_year')

        # Deleting field 'Composer.d_year'
        db.delete_column(u'rep_composer', 'd_year')

        # Adding field 'Composer.first_name'
        db.add_column(u'rep_composer', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=25),
                      keep_default=False)

        # Adding field 'Composer.last_name'
        db.add_column(u'rep_composer', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=25),
                      keep_default=False)

        # Adding field 'Composer.birth_year'
        db.add_column(u'rep_composer', 'birth_year',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4),
                      keep_default=False)

        # Adding field 'Composer.death_year'
        db.add_column(u'rep_composer', 'death_year',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Composer.l_name'
        raise RuntimeError("Cannot reverse this migration. 'Composer.l_name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Composer.l_name'
        db.add_column(u'rep_composer', 'l_name',
                      self.gf('django.db.models.fields.CharField')(max_length=25),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Composer.f_name'
        raise RuntimeError("Cannot reverse this migration. 'Composer.f_name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Composer.f_name'
        db.add_column(u'rep_composer', 'f_name',
                      self.gf('django.db.models.fields.CharField')(max_length=25),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Composer.b_year'
        raise RuntimeError("Cannot reverse this migration. 'Composer.b_year' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Composer.b_year'
        db.add_column(u'rep_composer', 'b_year',
                      self.gf('django.db.models.fields.IntegerField')(max_length=4),
                      keep_default=False)

        # Adding field 'Composer.d_year'
        db.add_column(u'rep_composer', 'd_year',
                      self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Composer.first_name'
        db.delete_column(u'rep_composer', 'first_name')

        # Deleting field 'Composer.last_name'
        db.delete_column(u'rep_composer', 'last_name')

        # Deleting field 'Composer.birth_year'
        db.delete_column(u'rep_composer', 'birth_year')

        # Deleting field 'Composer.death_year'
        db.delete_column(u'rep_composer', 'death_year')


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
            'librettist_fname': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'librettist_lname': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['rep']