from django.db import models
from account.models import User

class PostAbstract(models.Model):
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class LikeDislikeAbstract(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_dislike = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Twit(PostAbstract):

    def __str__(self):
        return f'{self.author} - {self.text}'



class TwitLikeDislike(LikeDislikeAbstract):
    twit = models.ForeignKey(Twit, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.author} - {self.twit.id} - {self.is_dislike}'


class Comment(PostAbstract):
    twit = models.ForeignKey(Twit, on_delete=models.CASCADE)


    def __str__(self):
        return f'comment {self.twit.id} - {self.text} - {self.author}'


class CommentLikeDislike(LikeDislikeAbstract):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.comment.id} - {self.is_dislike}'

