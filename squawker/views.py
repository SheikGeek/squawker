from django.template import Context, loader
from django.http import HttpResponse
import datetime

def current_datetime(request):
	now = datetime.datetime.now()
	template = loader.get_template('index.html')
	context = Context({
		'now': now,
	})
	return HttpResponse(template.render(context))
