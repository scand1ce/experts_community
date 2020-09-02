from django.urls import path


from .views import (
    AdminUsersListView,
    AdminCreateUserView,
    AdminUserDeleteView,
    AdminUpdateUserView
)


urlpatterns = [
    path('user/updade/<int:pk>/', AdminUpdateUserView.as_view(), name='admin_update_users'),
    path('user/delete/<int:pk>/', AdminUserDeleteView.as_view(), name='admin_delete_users'),
    path('create-user/', AdminCreateUserView.as_view(), name='admin_create_users'),
    path('my-admin/', AdminUsersListView.as_view(), name='admin_page'),
    #  path('my-admin/', views.get_user_list, name='admin_page'),
]
