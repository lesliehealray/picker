# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Song'
        db.create_table(u'rep_song', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('composer', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('librettist_fname', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('librettist_lname', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal(u'rep', ['Song'])

        # Adding model 'Program'
        db.create_table(u'rep_program', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('create_date', self.gf('django.db.models.fields.DateField')()),
            ('perf_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'rep', ['Program'])

        # Adding model 'Composer'
        db.create_table(u'rep_composer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('f_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('l_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('b_year', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('d_year', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
        ))
        db.send_create_signal(u'rep', ['Composer'])

        # Adding model 'ProgramSong'
        db.create_table(u'rep_programsong', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('song', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rep.Song'])),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rep.Program'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'rep', ['ProgramSong'])


    def backwards(self, orm):
        # Deleting model 'Song'
        db.delete_table(u'rep_song')

        # Deleting model 'Program'
        db.delete_table(u'rep_program')

        # Deleting model 'Composer'
        db.delete_table(u'rep_composer')

        # Deleting model 'ProgramSong'
        db.delete_table(u'rep_programsong')


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
            'composer': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'librettist_fname': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'librettist_lname': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['rep']