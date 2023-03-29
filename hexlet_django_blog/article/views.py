from django.shortcuts import render
from django.views import View


class ArticleIndex(View):

    def get(self, request):
        return render(
            request,
            'article/index.html',
            context={'app_name': 'Article-dramaticle'},
        )
