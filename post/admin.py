from django.contrib import admin

from .models import Twit, Comment, CommentLikeDislike, TwitLikeDislike

admin.site.register(Twit)
admin.site.register(Comment)
admin.site.register(CommentLikeDislike)
admin.site.register(TwitLikeDislike)


