from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout

#for pusher photo feed
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from pusher import Pusher

from django.utils.safestring import mark_safe

import json

from . import models
from . import forms

from .models import Feed
from .forms import DocumentForm

from django.contrib.auth.decorators import login_required

# instantiate pusher
pusher = Pusher(app_id=u'id', key=u'key', secret=u'secret :)', cluster=u'us2')

# Create your views here.


def about(request):
    PreviousEvent = models.PreviousEvents.objects.all().order_by('-id').reverse()
    PreviousPerformer = models.PreviousPerformers.objects.all().order_by('-id')
    context = {
        "title":"About Oasis",
        "event_info": PreviousEvent,
        "performer_info": PreviousPerformer
        }
    return render(request, "sections/about.html", context=context)

def news(request):
    NewPost = models.NewsPost.objects.all().order_by('-id')
    context = {
        "title":"News",
        "info": NewPost
        }
    return render(request, "sections/news.html", context=context)

# views for archive
def archive(request):
    if request.user.is_authenticated:
        all_documents = models.Feed.objects.filter(author=request.user).order_by('-id')
        context = {
            "title":"Archive",
            "all_documents": all_documents
            }
        return render(request, "sections/archive.html", context=context)
    else:
        context = {"title":"Archive"}
        return render(request, "sections/archive.html", context=context)

def archive_year(request, year):
    NewPost = models.NewsPost.objects.all().order_by('-id')
    year_docs = models.Feed.objects.filter(creation_year=year).order_by('-id')
    context = {
        "title":"Archive",
        "page":year,
        "info": NewPost,
        "year_docs": year_docs
        }
    return render(request, "sections/archive.html", context=context)

# views for account management
def logout_view(request):
    logout(request)
    return redirect("/login/")

def register(request):
    if request.method == 'POST':
        regisration_form = forms.RegistrationForm(request.POST)
        if regisration_form.is_valid():
            regisration_form.save(commit=True)
            return redirect("/login/")
    else:
        regisration_form = forms.RegistrationForm()
    context = {"form":regisration_form}
    return render(request, "registration/register.html", context=context)

#views for live chat
def help(request):
    return render(request, 'sections/help.html', {})

def room(request, room_name):
    if request.user.is_authenticated:
        return render(request, 'sections/rooms.html', {
            'room_name': room_name,
            'room_name_json': mark_safe(json.dumps(room_name))
        })
    else:
        return redirect("/login/")

# views for pusher photo feed

def index(request):
        # get all current photos ordered by the latest
        all_documents = Feed.objects.all().order_by('-id')
        context = {
            "all_documents": all_documents
            }
        # return the index.html template, passing in all the feeds
        return render(request, 'index.html', context=context)

#function that authenticates the private channel
def pusher_authentication(request):
    channel = request.GET.get('channel_name', None)
    socket_id = request.GET.get('socket_id', None)
    auth = pusher.authenticate(
      channel = channel,
      socket_id = socket_id
    )

    return JsonResponse(json.dumps(auth), safe=False)

#function that triggers the pusher request
def push_feed(request):
    # check if the method is post
    if request.method == 'POST':
        # try form validation
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(request.user, commit=True)
            # trigger a pusher request after saving the new feed element
            pusher.trigger(u'a_channel', u'an_event', {u'document': f.document.url})
            return HttpResponse('ok')
        else:
            # return a form not valid error
            return HttpResponse('form not valid')
    else:
        # return error, type isnt post
        return HttpResponse('error, please try again')
