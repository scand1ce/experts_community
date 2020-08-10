from django.urls import path

from . views import get_user_list

urlpatterns = [
    path('my-admin/', get_user_list, name='admin_page'),
]
