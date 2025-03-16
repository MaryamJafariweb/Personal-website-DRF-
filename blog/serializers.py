from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('author', 'title', 'img', 'body', 'created', 'comments')

    def get_comments(self, object):
        result = object.post_comments.all()
        return CommentSerializer(instance=result, many=True).data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('author', 'body')
