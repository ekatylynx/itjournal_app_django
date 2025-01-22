from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout

from .models import News, Category
from .forms import NewsForm, CustomUserCreationForm, UserLoginForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created!')
            user = form.save()
            login(request, user)
        else:
            messages.error(request, 'Error!')
            print(form.errors)  # Выводим ошибки валидации для отладки
    else:
        form = CustomUserCreationForm()
    return render(request, 'News/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home')
    else:
        form = UserLoginForm()
    return render(request, 'News/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('Home')


class HomeNews(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'News/index.html'
    extra_content = {'title': 'Home'}
    paginate_by = 3

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home Page'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')

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
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')

class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    template_name = 'News/view_news.html'

class AddNews(CreateView):
    form_class = NewsForm
    template_name = 'News/add_news.html'
    login_url = '/admin/'

# Custom Page 404
def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})
