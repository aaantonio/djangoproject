from django.shortcuts import render
<<<<<<< HEAD
from django.views.generic import CreateView
# Create your views here.
from .models import Book, Publisher, Author

class AuthorCreateView(CreateView):
    template_name = 'authorcreateview.html'
    model = Author
    fields = ['first_name', 'last_name', 'email']
=======
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Author, Publisher, Book

# Create your views here.
class AuthorCreateView(CreateView):
	template_name = 'authorcreate.html'
	model = Author
	fields = ['first_name', 'last_name', 'email']
	success_url = '/author'

class AuthorListView(ListView):
	template_name = 'authors.html'
	queryset = Author.objects.all().order_by('-pk')

class AuthorDetailView(DetailView):
	model = Author
	template_name = 'authors.html'

class AuthorUpdateView(UpdateView):
	template_name = 'authorcreate.html'
	model = Author
	fields = ['first_name', 'last_name', 'email']

	# def get_success_url(self):
	# 	return reverse('AuthorDetail', kwargs={'pk': self.object.pk})
	

class AuthorDeleteView(DeleteView):
	model = Author
	success_url = '/author'
>>>>>>> 9f96e9d2a602f6bb778c5b4fa7d599ef5718c7d3
