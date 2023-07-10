from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.book_list, name='list'),
    path('new/', views.book_new, name='book_new'),
    url('author/create', views.author_create_popup, name = "author_create"),
    url('publisher/create', views.publisher_create_popup, name = "publisher_create"),
    url('genre/create', views.genre_create_popup, name = "genre_create"),
]
