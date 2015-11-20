# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'User.username'
        db.alter_column(u'main_user', 'username', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'User.username'
        db.alter_column(u'main_user', 'username', self.gf('django.db.models.fields.CharField')(max_length=40))

    models = {
        'main.following': {
            'Meta': {'object_name': 'Following'},
            'follower': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_following_related'", 'to': u"orm['main.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seed_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.User']"})
        },
        'main.result': {
            'Meta': {'object_name': 'Result'},
            'follower': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_result_related'", 'to': u"orm['main.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stockmarket': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'main.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'follower': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_tweet_related'", 'to': u"orm['main.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seed_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.User']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'main.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'r'", 'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['main']