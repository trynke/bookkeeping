from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.book_list, name='list'),
    path('new/', views.book_new, name='book_new'),
    re_path('author/create', views.author_create_popup, name = "author_create"),
    re_path('publisher/create', views.publisher_create_popup, name = "publisher_create"),
    re_path('genre/create', views.genre_create_popup, name = "genre_create"),
]
