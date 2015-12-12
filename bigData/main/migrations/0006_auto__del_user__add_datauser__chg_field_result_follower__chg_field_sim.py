# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'main_user')

        # Adding model 'DataUser'
        db.create_table(u'main_datauser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.CharField')(default='r', max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['DataUser'])


        # Changing field 'Result.follower'
        db.alter_column(u'main_result', 'follower_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.DataUser']))

        # Changing field 'SimilarSeedUser.seed_user_one'
        db.alter_column(u'main_similarseeduser', 'seed_user_one_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.DataUser']))

        # Changing field 'SimilarSeedUser.seed_user_two'
        db.alter_column(u'main_similarseeduser', 'seed_user_two_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.DataUser']))

        # Changing field 'SeedFollowerRank.seed_user'
        db.alter_column(u'main_seedfollowerrank', 'seed_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.DataUser']))

        # Changing field 'RecommendationTwo.follower'
        db.alter_column(u'main_recommendationtwo', 'follower_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.DataUser']))

        # Changing field 'RecommendationTwo.seed_user'
        db.alter_column(u'main_recommendationtwo', 'seed_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.DataUser']))

        # Changing field 'SimilarFollower.follower_one'
        db.alter_column(u'main_similarfollower', 'follower_one_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.DataUser']))

        # Changing field 'SimilarFollower.follower_two'
        db.alter_column(u'main_similarfollower', 'follower_two_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.DataUser']))

        # Changing field 'Tweet.seed_user'
        db.alter_column(u'main_tweet', 'seed_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.DataUser']))

        # Changing field 'Tweet.follower'
        db.alter_column(u'main_tweet', 'follower_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.DataUser']))

        # Changing field 'RecommendationOne.follower'
        db.alter_column(u'main_recommendationone', 'follower_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.DataUser']))

        # Changing field 'RecommendationOne.seed_user'
        db.alter_column(u'main_recommendationone', 'seed_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.DataUser']))

        # Changing field 'Following.seed_user'
        db.alter_column(u'main_following', 'seed_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.DataUser']))

        # Changing field 'Following.follower'
        db.alter_column(u'main_following', 'follower_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.DataUser']))

    def backwards(self, orm):
        # Adding model 'User'
        db.create_table(u'main_user', (
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.CharField')(default='r', max_length=2, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'main', ['User'])

        # Deleting model 'DataUser'
        db.delete_table(u'main_datauser')


        # Changing field 'Result.follower'
        db.alter_column(u'main_result', 'follower_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

        # Changing field 'SimilarSeedUser.seed_user_one'
        db.alter_column(u'main_similarseeduser', 'seed_user_one_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

        # Changing field 'SimilarSeedUser.seed_user_two'
        db.alter_column(u'main_similarseeduser', 'seed_user_two_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

        # Changing field 'SeedFollowerRank.seed_user'
        db.alter_column(u'main_seedfollowerrank', 'seed_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

        # Changing field 'RecommendationTwo.follower'
        db.alter_column(u'main_recommendationtwo', 'follower_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

        # Changing field 'RecommendationTwo.seed_user'
        db.alter_column(u'main_recommendationtwo', 'seed_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

        # Changing field 'SimilarFollower.follower_one'
        db.alter_column(u'main_similarfollower', 'follower_one_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

        # Changing field 'SimilarFollower.follower_two'
        db.alter_column(u'main_similarfollower', 'follower_two_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

        # Changing field 'Tweet.seed_user'
        db.alter_column(u'main_tweet', 'seed_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

        # Changing field 'Tweet.follower'
        db.alter_column(u'main_tweet', 'follower_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

        # Changing field 'RecommendationOne.follower'
        db.alter_column(u'main_recommendationone', 'follower_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

        # Changing field 'RecommendationOne.seed_user'
        db.alter_column(u'main_recommendationone', 'seed_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

        # Changing field 'Following.seed_user'
        db.alter_column(u'main_following', 'seed_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

        # Changing field 'Following.follower'
        db.alter_column(u'main_following', 'follower_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User']))

    models = {
        u'main.datauser': {
            'Meta': {'object_name': 'DataUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'r'", 'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.following': {
            'Meta': {'object_name': 'Following'},
            'follower': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_following_related'", 'to': u"orm['main.DataUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seed_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.DataUser']"})
        },
        'main.recommendationone': {
            'Meta': {'object_name': 'RecommendationOne'},
            'follower': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_recommendationone_related'", 'to': u"orm['main.DataUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seed_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.DataUser']"})
        },
        'main.recommendationtwo': {
            'Meta': {'object_name': 'RecommendationTwo'},
            'follower': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_recommendationtwo_related'", 'to': u"orm['main.DataUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seed_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.DataUser']"})
        },
        'main.result': {
            'Meta': {'object_name': 'Result'},
            'follower': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_result_related'", 'to': u"orm['main.DataUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stockmarket': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'main.seedfollowerrank': {
            'Meta': {'object_name': 'SeedFollowerRank'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_of_followers': ('django.db.models.fields.IntegerField', [], {}),
            'rank': ('django.db.models.fields.IntegerField', [], {}),
            'seed_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.DataUser']"})
        },
        'main.similarfollower': {
            'Meta': {'object_name': 'SimilarFollower'},
            'follower_one': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.DataUser']"}),
            'follower_two': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_similarfollower_related'", 'to': u"orm['main.DataUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'similarity_score': ('django.db.models.fields.IntegerField', [], {})
        },
        'main.similarseeduser': {
            'Meta': {'object_name': 'SimilarSeedUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seed_user_one': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.DataUser']"}),
            'seed_user_two': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_similarseeduser_related'", 'to': u"orm['main.DataUser']"}),
            'similarity_score': ('django.db.models.fields.IntegerField', [], {})
        },
        'main.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'follower': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'main_tweet_related'", 'to': u"orm['main.DataUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seed_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.DataUser']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['main']