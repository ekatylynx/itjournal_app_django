from django.urls import path
from News.views import HomeNews, NewsByCategory, ViewNews, AddNews, register, user_login, user_logout
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', HomeNews.as_view(), name='Home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='Category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='View_news'),
    path('news/add_news', AddNews.as_view(), name='Add_news'),
    path('signup/', register, name='Register'),
    path('signin/', user_login, name='Login'),
    path('logout/', user_logout, name='Logout'),
]
