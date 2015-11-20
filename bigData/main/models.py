#from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _


class User(models.Model):
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

#def create_extended_user(sender, instance, created, **kwargs):
#    if created:
#       user, created = ExtendedUser.objects.get_or_create(user=instance)

#post_save.connect(create_extended_user, sender=User)


class Tweet( models.Model ):
    """
    The tweet class saves the data extracted from Twitter.
    """

    seed_user = models.ForeignKey(User)
    follower = models.ForeignKey(User, related_name = "%(app_label)s_%(class)s_related")
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

    seed_user = models.ForeignKey(User)
    follower = models.ForeignKey(User, related_name = "%(app_label)s_%(class)s_related")

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

    follower = models.ForeignKey(User, related_name = "%(app_label)s_%(class)s_related")
    stockmarket = models.BooleanField(default = False)

    def __unicode__(self):
        return _("%s_%s") % (self.follower, self.stockmarket)

    class Meta:
        app_label = "main"
        verbose_name = "result"
        verbose_name_plural = "results"