from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (CreateView, ListView, UpdateView, DeleteView)
from users.models import CustomUser


class AdminCreateUserView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = CustomUser
    success_url = reverse_lazy('admin_page')
    template_name = 'admin/admin_create_users.html'
    fields = [
        'username',
        'email',
        'department',
        'password',
        'is_active',
        'is_staff'
    ]

    def test_func(self):
        if self.request.user.is_active and self.request.user.is_staff:
            return True
        return False


class AdminUsersListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = CustomUser
    template_name = 'admin/admin_page.html'

    def test_func(self):
        if self.request.user.is_active and self.request.user.is_staff:
            return True
        return False


class AdminUpdateUserView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    success_url = reverse_lazy('admin_page')
    template_name = 'admin/admin_update_users.html'
    fields = ['is_active', 'is_staff', 'body']

    def test_func(self):
        if self.request.user.is_active and self.request.user.is_staff:
            return True
        return False


class AdminUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CustomUser
    success_url = reverse_lazy('admin_page')
    template_name = 'admin/admin_delete_users.html'

    def test_func(self):
        if self.request.user.is_active and self.request.user.is_staff:
            return True
        return False
