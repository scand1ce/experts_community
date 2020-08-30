
from django.urls import path
from posts.views import CreatePostsView, ListPostsView

urlpatterns = [
    path('posts/', ListPostsView.as_view(), name='list_posts'),
    path('post/new/', CreatePostsView.as_view(), name='create_posts'),
]



