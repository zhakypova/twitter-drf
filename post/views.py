from django.shortcuts import render
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import views
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Twit, Comment, TwitLikeDislike, CommentLikeDislike
from .serializers import TwitSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

class TwitViewSet(viewsets.ModelViewSet):
    queryset = Twit.objects.all()
    serializer_class = TwitSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [IsAuthenticatedOrReadOnly | IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = TwitSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [IsAuthenticatedOrReadOnly | IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikeTwitAPIView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [IsAuthenticatedOrReadOnly | IsAuthorOrReadOnly]

    def post(self, request, *args, **kwargs):
        twit_id = kwargs.get('twit_id')
        author = request.user
        dislike = kwargs.get('dislike')
        new_like_dislike_twit = TwitLikeDislike(
            twit_id=twit_id,
            author=author,
            is_dislike=dislike
        )
        new_like_dislike_twit.save()
        return Response(status=200)


class LikeCommentAPIView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [IsAuthenticatedOrReadOnly | IsAuthorOrReadOnly]

    def post(self, request, *args, **kwargs):
        comment_id = kwargs.get('comment_id')
        author = request.user
        dislike = kwargs.get('dislike')
        like_dislike_comment = CommentLikeDislike(
            comment_id=comment_id,
            author=author,
            is_dislike=dislike
        )
        like_dislike_comment.save()
        return Response(status=200)
