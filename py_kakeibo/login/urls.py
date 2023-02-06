from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = 'login'
# http://localhost:8000/login/~で表示するurlたち
urlpatterns = [
   path('', views.login, name='login'),
   path("login/", auth_views.LoginView.as_view(template_name="login/login.html"), name="login"),
   path("logout/", auth_views.LogoutView.as_view(), name="logout"),
   path("signup/", views.signup, name="signup"),
]