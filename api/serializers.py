from rest_framework import serializers
from posts.models import Post
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser

        fields = (

            "username",
        )


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('author', 'title', 'created_at',)
