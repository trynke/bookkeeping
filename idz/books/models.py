from django.conf import settings
from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=200, blank=False)
    
    def __str__(self):
        return self.author_name


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=200, blank=False)
    
    def __str__(self):
        return self.publisher_name


class Genre(models.Model):
    genre_title = models.CharField(max_length=200, blank=False)
    
    def __str__(self):
        return self.genre_title


class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    author = models.ManyToManyField(Author, blank=False)
    publisher = models.ManyToManyField(Publisher, blank=False)
    genre = models.ManyToManyField(Genre, blank=False)
    pages = models.IntegerField(blank=True)
    year = models.CharField(max_length=4, blank=True)
    isbn = models.CharField(max_length=30, blank=True)
    binging = models.CharField(max_length=200, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
