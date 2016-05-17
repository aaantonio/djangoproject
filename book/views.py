from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Author, Publisher, Book

# Create your views here.
class AuthorCreateView(CreateView):
	template_name = 'authorcreate.html'
	model = Author
	fields = ['first_name', 'last_name', 'email']
	success_url = '/'

class AuthorListView(ListView):
	pass
