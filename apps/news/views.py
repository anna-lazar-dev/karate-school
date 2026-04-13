from django.shortcuts import render, get_object_or_404
from apps.news.models import News


def news_list_view(request):
    news_list = News.objects.filter(is_published=True)

    context = {
        'news_list': news_list,
    }
    return render(request, 'news/news_list.html', context)


def news_detail_view(request, pk):
    news_item = get_object_or_404(News, pk=pk, is_published=True)

    context = {
        'news_item': news_item,
    }
    return render(request, 'news/news_detail.html', context)