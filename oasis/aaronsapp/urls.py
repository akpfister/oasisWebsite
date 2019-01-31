from django.urls import path, include

from . import views
from aaronsapp.views import *
from django.contrib.auth import views as adminviews

from django.conf import settings
from django.conf.urls.static import static

#for pusher photo feed
# from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', adminviews.LoginView.as_view()),
    path('logout/', views.logout_view),
    path('about/', views.about),
    path('news/', views.news),

    #archive pages
    path('archive/', views.archive),
    path('archive/<int:year>/', views.archive_year),

    #chat system
    path('help/', views.help),
    path('help/<room_name>/', views.room),

    #photo feed
    path('push_feed', push_feed),\
    path('pusher_authentication', pusher_authentication),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
