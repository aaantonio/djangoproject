from django.views.generic import TemplateView, CreateView, ListView
from datetime import datetime, timedelta
from book.models import Author, Publisher, Book

class MyView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(MyView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

class PlusTime(TemplateView):
	template_name = 'plus.html'

	def get_context_data(self, **kwargs):
		context = super(PlusTime, self).get_context_data(**kwargs)
		try:
			context['plus'] = datetime.now() + timedelta(hours=int(self.kwargs['plus']))
		except:
			context['plus'] = datetime.now()
		return context

class AuthorCreate(CreateView):
	model = Author
	template_name = 'authorcreate.html'
	fields = ['first_name', 'last_name', 'email']
	success_url = '/author'

class AuthorView(ListView):
	model = Author
	template_name = 'author.html'
	context_object_name = 'author'