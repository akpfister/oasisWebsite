from django.db import models

import datetime

from django.contrib.auth.models import User

# from model_utils import Choices

# Create your models here.

# News Section
class NewsPost(models.Model):
    date_announced = models.DateField()
    news = models.CharField("News:", max_length=300)
    name = models.CharField("Name:", max_length=50)
    position = models.CharField("Position:", max_length=20)
    document = models.FileField(upload_to='news_photos/', blank=True)

    def __str__(self):
        return self.news

# About Section

#Model for previous Oasis Events
class PreviousEvents(models.Model):
    date_of_event = models.CharField("Month Year:", max_length=30)
    summary = models.CharField("Event Summary:", max_length=300)
    leader = models.CharField("Event Organizer:", max_length=50)
    mainstage = models.CharField("List all performers from the main stage:", max_length=100)
    bunker = models.CharField("List all performers from the Deephouse Bunker:", max_length=100)

    def __str__(self):
        return self.date_of_event

# Model for previous Oasis performers
class PreviousPerformers(models.Model):
    performer_name = models.CharField("Performers Name:", max_length=50)
    performer_pic = models.FileField(upload_to='performer_photos/', blank=True)
    date_performed = models.CharField("Month Year that they performed:", max_length=100)
    performer_url = models.CharField("Give a link to the performers social media:", max_length=200)

    def __str__(self):
        return self.performer_name

# Home page section

#for creating the photo feed using pusher
class Feed(models.Model):
    #description = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.FileField(upload_to='photo_feed/')
    creation_date = models.DateField(auto_now_add=True)
    #creation_year = models.DateField(default=datetime.date.today().year)
    YEAR = (
        (2016, '2016'),
        (2017, '2017'),
        (2018, '2018'),
    )
    creation_year = models.IntegerField(default=2018, choices=YEAR)

    def __str__(self):
        return "Posed by: %s" % (self.author)
