from django.urls import path


from .views import (
    AdminUsersListView,
    AdminCreateUserView,
    AdminUserDeleteView,
    AdminUpdateUserView
)


urlpatterns = [
    path('user/<int:pk>/update/', AdminUpdateUserView.as_view(), name='admin_update_user'),
    path('user/<int:pk>/delete/', AdminUserDeleteView.as_view(), name='admin_delete_user'),
    path('create-user/', AdminCreateUserView.as_view(), name='admin_create_user'),
    path('my-admin/', AdminUsersListView.as_view(), name='admin_page'),
    #  path('my-admin/', views.get_user_list, name='admin_page'),
]
