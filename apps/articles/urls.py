from django.urls import path

from apps.articles.views import article_1, article_2

urlpatterns =[
    path('article1/', article_1),
    path('article2/', article_2),
]