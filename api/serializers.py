from rest_framework import serializers
from posts.models import Post
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser

        fields = (
            "first_name",
            "last_name"
            # "username",
        )


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('author', 'title', 'content', 'created_at',)
