from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView

)
from django.views.generic.edit import FormMixin
from posts.forms import CreatePostsForm, CreateCommentsForm
from posts.models import Post
from django.core.paginator import Paginator


class CreatePostsView(LoginRequiredMixin, CreateView):
    form_class = CreatePostsForm
    success_url = reverse_lazy('list_posts')
    template_name = 'posts/posts_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListPostsView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 2
    template_name = 'posts/posts_list.html'


class DetailPostsView(FormMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    form_class = CreateCommentsForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail_post', kwargs={'pk': self.get_object().pk})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class UpdatePostsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    success_url = reverse_lazy('list_posts')
    template_name = 'posts/post_update.html'
    fields = ('title', 'content', 'photo', 'is_published')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeletePostsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('list_posts')
    template_name = 'posts/post_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
