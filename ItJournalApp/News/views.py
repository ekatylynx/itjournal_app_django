from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import News, Category
from .forms import NewsForm

# Create your views here.

def index(request):
    news = News.objects.all()
    categories = Category.objects.all()

    context = {
        'news': news,
        'title': 'Stories for you',
    }

    return render(request, 'News/index.html', context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id = category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category
    }

    return render(request, 'News/category.html', context = context)

def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    context = {
        'news_item': news_item,
    }
    return render(request, 'News/view_news.html', context = context)


def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'News/add_news.html', {'form': form})