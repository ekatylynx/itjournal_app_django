from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from .models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'News/index.html'
    extra_content = {'title': 'Home'}

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home Page'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)

class NewsByCategory(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'News/category.html'
    allow_empty = False

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    template_name = 'News/view_news.html'

class AddNews(CreateView):
    form_class = NewsForm
    template_name = 'News/add_news.html'

# Custom Page 404
def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})
