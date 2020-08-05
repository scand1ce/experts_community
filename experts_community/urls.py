# from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from my_admin import views

urlpatterns = [
    path('my_admin/', views.user_, name='admin_page'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

]
