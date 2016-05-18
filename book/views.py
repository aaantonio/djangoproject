from django.shortcuts import render
from django.views.generic import CreateView
# Create your views here.
from .models import Book, Publisher, Author

class AuthorCreateView(CreateView):
    template_name = 'authorcreateview.html'
    model = Author
    fields = ['first_name', 'last_name', 'email']