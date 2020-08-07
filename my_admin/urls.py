from django.urls import path

from . views import get_user_list

urlpatterns = [
    path('my_admin/', get_user_list, name='admin_page'),
]
