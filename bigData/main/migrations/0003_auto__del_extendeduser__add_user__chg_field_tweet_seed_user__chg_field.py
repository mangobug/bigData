# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ExtendedUser'
        db.delete_table(u'main_extendeduser')

        # Adding model 'User'
        db.create_table(u'main_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('type', self.gf('django.db.models.fields.CharField')(default='r', max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['User'])


        # Changing field 'Tweet.seed_user'
        db.alter_column(u'main_tweet', 'seed_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

        # Changing field 'Tweet.follower'
        db.alter_column(u'main_tweet', 'follower_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

        # Changing field 'Following.seed_user'
        db.alter_column(u'main_following', 'seed_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

        # Changing field 'Following.follower'
        db.alter_column(u'main_following', 'follower_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

        # Changing field 'Result.follower'
        db.alter_column(u'main_result', 'follower_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

    def backwards(self, orm):
        # Adding model 'ExtendedUser'
        db.create_table(u'main_extendeduser', (
            ('type', self.gf('django.db.models.fields.CharField')(default='r', max_length=2, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'main', ['ExtendedUser'])

        # Deleting model 'User'
        db.delete_table(u'main_user')


        # Changing field 'Tweet.seed_user'
        db.alter_column(u'main_tweet', 'seed_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Tweet.follower'
        db.alter_column(u'main_tweet', 'follower_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Following.seed_user'
        db.alter_column(u'main_following', 'seed_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Following.follower'
        db.alter_column(u'main_following', 'follower_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Result.follower'
        db.alter_column(u'main_result', 'follower_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

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
            'username': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['main']