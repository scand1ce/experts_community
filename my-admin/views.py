from django.urls import reverse_lazy
from django.views.generic import (CreateView, ListView, UpdateView, DeleteView)

from users.models import CustomUser


class AdminCreateUserView(CreateView):
    model = CustomUser
    success_url = reverse_lazy('admin_page')
    template_name ='admin/admin_create_users.html'
    fields = [
        'username',
        'email',
        'department',
        'password',
        'is_active',
        'is_staff'
    ]


class AdminUsersListView(ListView):
    model = CustomUser
    template_name = 'admin/admin_page.html'


class AdminUpdateUserView(UpdateView):
    model = CustomUser
    success_url = reverse_lazy('admin_page')
    template_name ='admin/admin_update_users.html'
    fields = ['is_active', 'is_staff', 'body']


class AdminUserDeleteView(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('admin_page')
    template_name = 'admin/admin_delete_users.html'





