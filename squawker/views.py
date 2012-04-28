from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import Context, RequestContext, loader

def index(request):
	if request.method == "GET":
		context = {}
		context.update(csrf(request))
		if request.user.is_authenticated():
			user_id = request.session['_auth_user_id']
			if user_id:
				user = User.objects.get(id=user_id)	
				username = user.username
				context['username'] = username
		return render_to_response("index.html", context)
	else:
		username = request.POST['username']
		password = request.POST['password']
		
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				# now redirect to index
				return redirect('/')
			else:
				context = {}
				context['error'] = "User %s is disabled." % (username)
				context.update(csrf(request))
				# reload page with error text
				return render_to_response("index.html", context)
		else:
			# reload page with error text
			context = {}
			context['error'] = "Username or password was invalid. Please try again."
			context.update(csrf(request))
			# reload page with error text
			return render_to_response("index.html", context)

def create_user(request):
	if request.method == "GET":
		context = {}
		context.update(csrf(request))
		return render_to_response("create_user.html", context)
	else:
		username = request.POST['username']
		password = request.POST['password'].strip()
		password_confirm = request.POST['password_confirm'].strip()

		if password != password_confirm:
			context = {}
			context['username'] = username
			context['error'] = "Passwords do not match. Please try again."
			context.update(csrf(request))
			# reload page with error text
			return render_to_response("create_user.html", context)
		elif not username:
			context = {}
			context['error'] = "Username was blank. Please try again."
			context.update(csrf(request))
			# reload page with error text
			return render_to_response("create_user.html", context)
		elif password == '' or password_confirm == '':
			context = {}
			context['username'] = username
			context['error'] = "Password cannot be blank. Please try again."
			context.update(csrf(request))
			# reload page with error text
			return render_to_response("create_user.html", context)
		else:
			# username was not empty
			# passwords match, check if username already in use
			try:
				User.objects.get(username=username)
				context = {}
				context['error'] = "Username already exists. Please try again."
				context.update(csrf(request))
				# reload page with error text
				return render_to_response("create_user.html", context)
			# username not in use, so create it and log them in
			except User.DoesNotExist:
				User.objects.create_user(username, None, password) 
				user = authenticate(username=username, password=password)
				if user is not None:
					if user.is_active:
						auth_login(request, user)
						# now redirect to index
						return redirect('/')
					else:
						return HttpResponse(status=500)
				else:
					return HttpResponse(status=500)

# implemented by a POST request to the index page '/'
# leaving for legacy/clarity
'''
def login(request):
	# TODO implement
	return HttpResponse(status=404)
'''

def logout(request):
	auth_logout(request)
	return redirect('/')

