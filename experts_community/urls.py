# from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView



urlpatterns = [
    path('storage-app/', include('storage-app.urls')),
    path('my-admin/', include('my-admin.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]




