from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Article


class ArticleIndex(View):

    def get(self, request):
        articles = Article.objects.all()[:15]
        return render(
            request,
            'article/index.html',
            context={'articles': articles},
        )


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            'article/show.html',
            context={'article': article},
        )
