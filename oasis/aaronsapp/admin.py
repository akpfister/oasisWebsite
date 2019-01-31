from django.contrib import admin

from . import models
# Register your models here.

# News Section
admin.site.register(models.NewsPost)

# About Section
admin.site.register(models.PreviousEvents)

admin.site.register(models.PreviousPerformers)

# Photo Feed Section
admin.site.register(models.Feed)
