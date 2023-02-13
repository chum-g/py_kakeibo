from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

app_name = 'login'
# http://localhost:8000/login/~で表示するurlたち
urlpatterns = [
   # path('', views.login, name='login'),
   path('admin/', admin.site.urls),
   path('detail/', include('detail.urls')),
   path("", auth_views.LoginView.as_view(template_name="login/login.vue"), name="login"),
   path('index/', views.index, name='index'),
   path("logout/", auth_views.LogoutView.as_view(), name="logout"),
   path("signup/", views.signup, name="signup"),
]