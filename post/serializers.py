from rest_framework import serializers

from .models import Twit, Comment

class TwitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Twit
        fields = '__all__'
        read_only_fields = ['author', ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', ]
