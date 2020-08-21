from django.urls import path
from .views import SignUpView, HomePageView
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', HomePageView.as_view(), name='home'),
]
