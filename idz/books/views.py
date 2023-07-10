from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .forms import BookForm, AuthorForm, PublisherForm, GenreForm
from .models import Book, Author, Publisher, Genre

def book_list(request):
    if 'title' in request.GET:
        title = request.GET['title']

    if 'author' in request.GET:
        author = request.GET['author']

    if 'genre' in request.GET:
        genre = request.GET['genre']

    if 'year' in request.GET:
        year = request.GET['year']

    if 'publisher' in request.GET:
        publisher = request.GET['publisher']

        books = Book.objects.filter(
            title__icontains=title, 
            author__author_name__icontains=author,
            genre__genre_title__icontains=genre,
            year__icontains=year,
            publisher__publisher_name__icontains=publisher
            )

        if books.count() == 0:
            return render(request, 'books/noresults.html')
        else:
            return render(request, 'books/list.html', {'books': books})
    else:
        books = Book.objects.all()
        return render(request, 'books/list.html', {'books': books})


def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('list')
    else:
        form = BookForm()
    return render(request, 'books/book_new.html', {'form': form})


def author_create_popup(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_author");</script>' % (instance.pk, instance))

    return render(request, "books/author_form.html", {"form" : form})


def publisher_create_popup(request):
    form = PublisherForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_publisher");</script>' % (instance.pk, instance))

    return render(request, "books/publisher_form.html", {"form" : form})


def genre_create_popup(request):
    form = GenreForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_genre");</script>' % (instance.pk, instance))

    return render(request, "books/genre_form.html", {"form" : form})