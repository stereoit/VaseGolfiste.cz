# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GolfCourse'
        db.create_table('courses_golfcourse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('description', self.gf('ckeditor.fields.RichTextField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clubs.GolfClub'], blank=True)),
        ))
        db.send_create_signal('courses', ['GolfCourse'])


    def backwards(self, orm):
        # Deleting model 'GolfCourse'
        db.delete_table('courses_golfcourse')


    models = {
        'clubs.golfclub': {
            'Meta': {'object_name': 'GolfClub'},
            'description': ('ckeditor.fields.RichTextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'ASSOCIATED'", 'max_length': '10'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'courses.golfcourse': {
            'Meta': {'object_name': 'GolfCourse'},
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clubs.GolfClub']", 'blank': 'True'}),
            'description': ('ckeditor.fields.RichTextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['courses']