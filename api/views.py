from rest_framework import generics, permissions
from posts.models import Post
from .serializers import PostSerializer


class PostAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
