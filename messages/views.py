from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import Context, RequestContext, loader

# custome model imports
from messages.models import Message

# list messages
def list_messages(request):
    # TODO implement
    pass

# create a new message
def create_message(request):
    # only logged in users can write messages
    if request.user.is_authenticated():
        user_id = request.session['_auth_user_id']
        if request.method == "GET":
            context = {}
            context.update(csrf(request))
            return render_to_response("create_message.html", context)
        else:
            content = request.POST['message']
            # create the message
            message = Message(message=content, user_id=user_id)
            message.save()
    return redirect('/')
