#from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _


class DataUser(models.Model):
    """
    The table extends Django's user class.
    """
    TYPE_CHOICES = (
	    ('r', 'Root User'),
        ('f', 'Follower'),
    )
    username = models.CharField(max_length = 100)
    type = models.CharField(max_length = 2, choices = TYPE_CHOICES, blank = True, null = True, default = 'r')

    def __str__(self):  
          return _("%s's" ) % (self.username)


class Tweet( models.Model ):
    """
    The tweet class saves the data extracted from Twitter.
    """

    seed_user = models.ForeignKey(DataUser)
    follower = models.ForeignKey(DataUser, related_name = "%(app_label)s_%(class)s_related")
    text = models.TextField()
    date = models.DateTimeField(blank = True, null = True)

    def __unicode__(self):
        return _("%s") % (self.text)

    class Meta:
        app_label = "main"
        verbose_name = "tweet"
        verbose_name_plural = "tweets"


class Following( models.Model ):
    """
    The following class saves data based on our algorithm to determine who is following who.
    """

    seed_user = models.ForeignKey(DataUser)
    follower = models.ForeignKey(DataUser, related_name = "%(app_label)s_%(class)s_related")

    def __unicode__(self):
        return _("%s is followed by %s") % (self.seed_user, self.follower)

    class Meta:
        app_label = "main"
        verbose_name = "following"
        verbose_name_plural = "followings"


class Result( models.Model ):
    """
    The result class classifies users based on expert and novice in stockmarket.
    """

    follower = models.ForeignKey(DataUser, related_name = "%(app_label)s_%(class)s_related")
    stockmarket = models.BooleanField(default = False)

    def __unicode__(self):
        return _("%s_%s") % (self.follower, self.stockmarket)

    class Meta:
        app_label = "main"
        verbose_name = "result"
        verbose_name_plural = "results"


class SeedFollowerRank( models.Model ):
    """
    Rank the seed user based on the number of followers
    """

    seed_user = models.ForeignKey(DataUser)
    no_of_followers = models.IntegerField()
    rank = models.IntegerField()

    def __unicode__(self):
        return _("%s has a rank of %s") % (self.seed_user, self.rank)

    class Meta:
        app_label = "main"
        verbose_name = "rank"
        verbose_name_plural = "ranks"


class SimilarFollower( models.Model ):
    """
    Similar followers based on their similarity score
    """

    follower_one = models.ForeignKey(DataUser)
    follower_two = models.ForeignKey(DataUser, related_name = "%(app_label)s_%(class)s_related")
    similarity_score = models.IntegerField()

    def __unicode__(self):
        return _("%s and %s are similar") % (self.follower_one, self.follower_two)

    class Meta:
        app_label = "main"
        verbose_name = "follower recommendation"
        verbose_name_plural = "follower recommendation"


class SimilarSeedUser( models.Model ):
    """
    Similar seed users based on their similarity score
    """

    seed_user_one = models.ForeignKey(DataUser)
    seed_user_two = models.ForeignKey(DataUser, related_name = "%(app_label)s_%(class)s_related")
    similarity_score = models.IntegerField()

    def __unicode__(self):
        return _("%s and %s are similar") % (self.seed_user_one, self.seed_user_two)

    class Meta:
        app_label = "main"
        verbose_name = "seed user recommendation"
        verbose_name_plural = "seed user recommendation"


class RecommendationOne( models.Model ):
    """
    Recommendation system for followers and seed users
    """

    follower = models.ForeignKey(DataUser, related_name = "%(app_label)s_%(class)s_related")
    seed_user = models.ForeignKey(DataUser)

    def __unicode__(self):
        return _("User %s is recommended to follow %s") % (self.follower, self.seed_user)

    class Meta:
        app_label = "main"
        verbose_name = "recommendation system one"
        verbose_name_plural = "recommendations system one"


class RecommendationTwo( models.Model ):
    """
    Recommendation system for followers and seed users
    """

    follower = models.ForeignKey(DataUser, related_name = "%(app_label)s_%(class)s_related")
    seed_user = models.ForeignKey(DataUser)

    def __unicode__(self):
        return _("User %s is recommended to follow %s") % (self.follower, self.seed_user)

    class Meta:
        app_label = "main"
        verbose_name = "recommendation system two"
        verbose_name_plural = "recommendations system two"