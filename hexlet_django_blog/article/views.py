from django.shortcuts import render
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
