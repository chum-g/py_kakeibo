from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name='index'),
    # ex: /kakeibo/5/
    path('<int:date>/', views.detail_month, name='detail_month'),
    # ex: /kakeibo/5/results/
   #  path('<int:question_id>/results/', views.results, name='results'),
    # ex: /kakeibo/5/vote/
   #  path('<int:question_id>/vote/', views.vote, name='vote'),
]