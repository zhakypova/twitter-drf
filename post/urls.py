from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('tweet', views.TwitViewSet)
router.register('comment', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tweet/<int:twit_id>/<int:dislike>/', views.LikeTwitAPIView.as_view()),
    path('comment/<int:comment_id>/<int:dislike>/', views.LikeCommentAPIView.as_view()),

]
