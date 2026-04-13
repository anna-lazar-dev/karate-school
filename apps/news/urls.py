from django.urls import path
from apps.news.views import news_list_view, news_detail_view

app_name = 'news'

urlpatterns = [
    path('news/', news_list_view, name='list'),
    path('news/<int:pk>/', news_detail_view, name='detail'),
]