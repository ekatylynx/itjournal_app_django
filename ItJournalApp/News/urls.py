from django.urls import path
# from News.views import index, get_category, view_news, add_news
from News.views import HomeNews, NewsByCategory, view_news, add_news

urlpatterns = [
    # path('', index, name='Home'),
    path('', HomeNews.as_view(), name='Home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='Category'),
    path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/add_news', add_news, name='Add_news')
]
