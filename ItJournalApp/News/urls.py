from django.urls import path
from News.views import HomeNews, NewsByCategory, ViewNews, AddNews

urlpatterns = [
    path('', HomeNews.as_view(), name='Home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='Category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='View_news'),
    path('news/add_news', AddNews.as_view(), name='Add_news')
]
