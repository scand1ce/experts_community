from django.urls import path
from posts.views import CreatePostsView, ListPostsView, DitailPostsView

urlpatterns = [
    path('post/new/', CreatePostsView.as_view(), name='create_posts'),
    path('posts/', ListPostsView.as_view(), name='list_posts'),
    path('post/<int:pk>', DitailPostsView.as_view(), name='ditail_posts'),
]
