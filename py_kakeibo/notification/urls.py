from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

app_name = 'notification'
# http://localhost:8000/login/~で表示するurlたち
urlpatterns = [
   path(''                      , views.notification, name='notification'),
   path('<int:notification_id>/', views.detail      , name='notification_detail'),
]