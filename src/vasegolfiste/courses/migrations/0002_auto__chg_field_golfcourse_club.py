# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'GolfCourse.club'
        db.alter_column('courses_golfcourse', 'club_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clubs.GolfClub'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'GolfCourse.club'
        raise RuntimeError("Cannot reverse this migration. 'GolfCourse.club' and its values cannot be restored.")

    models = {
        'clubs.golfclub': {
            'Meta': {'object_name': 'GolfClub'},
            'description': ('ckeditor.fields.RichTextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'ASSOCIATED'", 'max_length': '10', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'courses.golfcourse': {
            'Meta': {'object_name': 'GolfCourse'},
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clubs.GolfClub']", 'null': 'True', 'blank': 'True'}),
            'description': ('ckeditor.fields.RichTextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['courses']