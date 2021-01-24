from rest_framework import generics, permissions
from posts.models import Post
from .serializers import PostSerializer
from .service import LargeResultsSetPagination


class PostAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    pagination_class = LargeResultsSetPagination
    serializer_class = PostSerializer
