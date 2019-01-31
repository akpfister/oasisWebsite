from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models
from .models import Feed

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user=super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

# #form for pusher photo feed
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Feed #models.Feed?
        fields = ('document', 'creation_year')
        #fields = ('description', 'document')

    #save user to the model
    def save(self, author, commit=True):
        document=super(DocumentForm, self).save(commit=False)
        document.author = author
        if commit:
            document.save()
        return document
