# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SimilarSeedUser'
        db.create_table(u'main_similarseeduser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seed_user_one', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User'])),
            ('seed_user_two', self.gf('django.db.models.fields.related.ForeignKey')(related_name='main_similarseeduser_related', to=orm['main.User'])),
            ('similarity_score', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('main', ['SimilarSeedUser'])

        # Adding model 'SeedFollowerRank'
        db.create_table(u'main_seedfollowerrank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seed_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User'])),
            ('no_of_followers', self.gf('django.db.models.fields.IntegerField')()),
            ('rank', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('main', ['SeedFollowerRank'])

        # Adding model 'RecommendationTwo'
        db.create_table(u'main_recommendationtwo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('follower', self.gf('django.db.models.fields.related.ForeignKey')(related_name='main_recommendationtwo_related', to=orm['main.User'])),
            ('seed_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User'])),
        ))
        db.send_create_signal('main', ['RecommendationTwo'])

        # Adding model 'RecommendationOne'
        db.create_table(u'main_recommendationone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('follower', self.gf('django.db.models.fields.related.ForeignKey')(related_name='main_recommendationone_related', to=orm['main.User'])),
            ('seed_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User'])),
        ))
        db.send_create_signal('main', ['RecommendationOne'])

        # Adding model 'SimilarFollower'
        db.create_table(u'main_similarfollower', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('follower_one', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User'])),
            ('follower_two', self.gf('django.db.models.fields.related.ForeignKey')(related_name='main_similarfollower_related', to=orm['main.User'])),
            ('similarity_score', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('main', ['SimilarFollower'])


    def backwards(self, orm):
        # Deleting model 'SimilarSeedUser'
        db.delete_table(u'main_similarseeduser')

        # Deleting model 'SeedFollowerRank'
        db.delete_table(u'main_seedfollowerrank')

        # Deleting model 'RecommendationTwo'
        db.delete_table(u'main_recommendationtwo')

        # Deleting model 'RecommendationOne'
        db.delete_table(u'main_recommendationone')

        # Deleting model 'SimilarFollower'
        db.delete_table(u'main_similarfollower')


    models = {
        'main.following': {
            'Meta': {'object_name': 'Following'},
            'follower': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_following_related'", 'to': u"orm['main.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seed_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.User']"})
        },
        'main.recommendationone': {
            'Meta': {'object_name': 'RecommendationOne'},
            'follower': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_recommendationone_related'", 'to': u"orm['main.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seed_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.User']"})
        },
        'main.recommendationtwo': {
            'Meta': {'object_name': 'RecommendationTwo'},
            'follower': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_recommendationtwo_related'", 'to': u"orm['main.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seed_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.User']"})
        },
        'main.result': {
            'Meta': {'object_name': 'Result'},
            'follower': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_result_related'", 'to': u"orm['main.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stockmarket': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'main.seedfollowerrank': {
            'Meta': {'object_name': 'SeedFollowerRank'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_of_followers': ('django.db.models.fields.IntegerField', [], {}),
            'rank': ('django.db.models.fields.IntegerField', [], {}),
            'seed_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.User']"})
        },
        'main.similarfollower': {
            'Meta': {'object_name': 'SimilarFollower'},
            'follower_one': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.User']"}),
            'follower_two': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_similarfollower_related'", 'to': u"orm['main.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'similarity_score': ('django.db.models.fields.IntegerField', [], {})
        },
        'main.similarseeduser': {
            'Meta': {'object_name': 'SimilarSeedUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seed_user_one': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.User']"}),
            'seed_user_two': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_similarseeduser_related'", 'to': u"orm['main.User']"}),
            'similarity_score': ('django.db.models.fields.IntegerField', [], {})
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