# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BarDuMonde.facebook'
        db.add_column(u'SHAKER_bardumonde', 'facebook',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'BarDuMonde.twitter'
        db.add_column(u'SHAKER_bardumonde', 'twitter',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BarDuMonde.facebook'
        db.delete_column(u'SHAKER_bardumonde', 'facebook')

        # Deleting field 'BarDuMonde.twitter'
        db.delete_column(u'SHAKER_bardumonde', 'twitter')


    models = {
        u'SHAKER.bardumonde': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'BarDuMonde', '_ormbases': [u'pages.Page']},
            'adresse': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'barman_vedette': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cocktail': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_derniere_visite': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'decoration': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'illustration': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'site_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'ville': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['SHAKER.Ville_BarDuMonde']"})
        },
        u'SHAKER.publicite': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Publicite', '_ormbases': [u'pages.Page']},
            'formatPub': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'lien': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'media': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'SHAKER.ville_bardumonde': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Ville_BarDuMonde', '_ormbases': [u'pages.Page']},
            'illustration': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['SHAKER']