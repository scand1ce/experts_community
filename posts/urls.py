from django.urls import path
from posts.views import (
    CreatePostsView,
    ListPostsView,
    DetailPostsView,
    UpdatePostsView,
    DeletePostsView
)

urlpatterns = [
    path('post/delete/<int:pk>/', DeletePostsView.as_view(), name='delete_post'),
    path('post/update/<int:pk>/', UpdatePostsView.as_view(), name='update_posts'),
    path('post/<int:pk>/', DetailPostsView.as_view(), name='detail_posts'),
    path('posts/', ListPostsView.as_view(), name='list_posts'),
    path('post/new/', CreatePostsView.as_view(), name='create_posts'),
]
