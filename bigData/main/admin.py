from django.contrib import admin

from bigData.main.models import User, Tweet, Following, Result


class UserAdmin(admin.ModelAdmin):
    pass

class TweetAdmin(admin.ModelAdmin):
    pass

class FollowingAdmin(admin.ModelAdmin):
    pass

class ResultAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Tweet, TweetAdmin)
admin.site.register(Following, FollowingAdmin)
admin.site.register(Result, ResultAdmin)