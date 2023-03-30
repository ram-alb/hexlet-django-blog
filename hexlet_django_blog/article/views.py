from django.shortcuts import render
from django.views import View


class ArticleIndex(View):

    def get(self, request, tags, article_id):
        return render(
            request,
            'article/index.html',
            context={'tags': tags, 'article_id': article_id},
        )
