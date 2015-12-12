from django.contrib import admin

from bigData.main.models import DataUser, Tweet, Following, Result, SeedFollowerRank, SimilarFollower, SimilarSeedUser, RecommendationOne, RecommendationTwo


class DataUserAdmin(admin.ModelAdmin):
    pass

class TweetAdmin(admin.ModelAdmin):
    pass

class FollowingAdmin(admin.ModelAdmin):
    pass

class ResultAdmin(admin.ModelAdmin):
    pass

class SeedFollowerRankAdmin(admin.ModelAdmin):
    pass

class SimilarFollowerAdmin(admin.ModelAdmin):
    pass

class SimilarSeedUserAdmin(admin.ModelAdmin):
    pass

class RecommendationOneAdmin(admin.ModelAdmin):
    pass

class RecommendationTwoAdmin(admin.ModelAdmin):
    pass

admin.site.register(DataUser, DataUserAdmin)
admin.site.register(Tweet, TweetAdmin)
admin.site.register(Following, FollowingAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(SeedFollowerRank, SeedFollowerRankAdmin)
admin.site.register(SimilarFollower, SimilarFollowerAdmin)
admin.site.register(SimilarSeedUser, SimilarSeedUserAdmin)
admin.site.register(RecommendationOne, RecommendationOneAdmin)
admin.site.register(RecommendationTwo, RecommendationTwoAdmin)