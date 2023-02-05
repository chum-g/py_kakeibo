from django.urls import path

from . import views

app_name = 'kakeibo'
# http://localhost:8000/kakeibo/~で表示するurlたち
urlpatterns = [
   path('', views.index, name='index'),
   # ex: /kakeibo/5/
   # path('<int:date>/', views.detail_month, name='detail'),
   path('detail/', views.detail_month, name='detail'),
   # ex: /kakeibo/5/results/
   #  path('<int:question_id>/results/', views.results, name='results'),
   # ex: /kakeibo/5/vote/
   #  path('<int:question_id>/vote/', views.vote, name='vote'),
   path('<int:year>/<int:month>/regist/', views.regist, name='regist'),
]