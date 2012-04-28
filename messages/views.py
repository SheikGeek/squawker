from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import Context, RequestContext, loader

# custom model imports
from messages.models import Message

# list messages
def list_messages(request):
	message_objects = Message.objects.all()
	messages = []
	for x in message_objects:
		user = User.objects.get(id=x.user_id)
		new_tuple = (x.message, user.username)
		messages.append(new_tuple)
	messages.reverse()
	# create the context for the template
	context = {}
	context['messages'] = messages
	return render_to_response("list_messages.html", context)

# create a new message
def create_message(request):
	# only logged in users can write messages
	if request.user.is_authenticated():
		user_id = request.session['_auth_user_id']
		if request.method == "GET":
			context = {}
			context.update(csrf(request))
			if user_id:
				user = User.objects.get(id=user_id)	
				username = user.username
				context['username'] = username
			return render_to_response("create_message.html", context)
		else:
			content = request.POST['message'].strip()
			if content == '':
				context = {}
				context['error'] = "Message cannot be blank. Please try again."
				context.update(csrf(request))
				if user_id:
					user = User.objects.get(id=user_id)	
					username = user.username
					context['username'] = username
				return render_to_response("create_message.html", context)
			# create the message
			message = Message(message=content, user_id=user_id)
			message.save()
	return redirect('/')
