from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,

)
from django.views.generic.edit import FormMixin
from posts.forms import CreatePostsForm, CreateCommentsForm
from posts.models import Post


class CreatePostsView(CreateView):
    form_class = CreatePostsForm
    success_url = reverse_lazy('list_posts')
    template_name = 'posts/posts_create.html'


class ListPostsView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'


class DetailPostsView(FormMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    form_class = CreateCommentsForm




class UpdatePostsView(UpdateView):
    model = Post
    success_url = reverse_lazy('list_posts')
    template_name = 'posts/post_update.html'
    fields = ('title', 'content', 'photo', 'is_published')
