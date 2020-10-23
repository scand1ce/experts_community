from django.urls import path
from .views import SignUpView, HomePageView, SearchResultsListView, UserDetailView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user_page'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('password', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', HomePageView.as_view(), name='home'),
]
