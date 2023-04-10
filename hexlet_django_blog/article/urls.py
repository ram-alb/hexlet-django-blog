from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.ArticleIndex.as_view(), name='article'),
    path('<int:id>/', views.ArticleView.as_view(), name='article-view'),
]
