from django.contrib import admin
from django.urls import include, path

# 8000/ でアクセス
urlpatterns = [
    path('detail/', include('detail.urls')),
    path('login/', include('login.urls')),
    path('notification/', include('notification.urls')),
    path('admin/', admin.site.urls),
    # path('', include('kakeibo.urls')),
]
