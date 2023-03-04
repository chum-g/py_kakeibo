from django.urls import path

from . import views

app_name = 'detail'
# http://localhost:8000/kakeibo/~で表示するurlたち
urlpatterns = [
   # path('', views.index, name='index'),
   # ex: /kakeibo/5/
   # path('<int:date>/', views.detail_month, name='detail'),
   # path(''                                , views.detail_month    , name='detail'),
   path('index/'                          , views.index            , name='index'),
   path('<int:year>/<int:month>/edit/'    , views.edit             , name='regist'),
   path('<int:year>/<int:month>/'         , views.summary_month_y_m, name=''),
   path('<int:year>/'                     , views.summary_year_y   , name=''),
   path('summary_month/'                  , views.summary_month    , name='summary_month'),
   path('summary_year/'                   , views.summary_year     , name='summary_year'),
   path('<int:item_id>/item_edit/'        , views.item_edit        , name='item_edit'),
   # ex: /kakeibo/5/results/
   #  path('<int:question_id>/results/', views.results, name='results'),
   # ex: /kakeibo/5/vote/
   #  path('<int:question_id>/vote/', views.vote, name='vote'),
]