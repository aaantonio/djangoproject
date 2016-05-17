from django.views.generic import TemplateView
from datetime import datetime, timedelta

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
