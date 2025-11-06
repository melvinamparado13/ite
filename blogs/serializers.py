from rest_framework import serializers
from .models import Blog, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        depth = 1

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Blog
        fields = "__all__"

    def create(self, validated_data):
        comments_data = validated_data.pop('comments', [])
        blog = Blog.objects.create(**validated_data)
        
        for comment_data in comments_data:
            Comment.objects.create(blog=blog, **comment_data)
        
        return blog
