from django.urls import path

from . import views

urlpatterns = [
    path('general/', views.chat, name='chat'),
]