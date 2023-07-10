from django.contrib import admin
from .models import Book, Author, Publisher, Genre

models = [Book, Author, Publisher, Genre]
for model in models:   
    admin.site.register(model)
