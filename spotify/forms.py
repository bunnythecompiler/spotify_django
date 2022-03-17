from django import forms 
from . models import SpotMusic 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SpotMusicForm(forms.ModelForm):

    class Meta:
        model = SpotMusic 
        fields = ['song_author',"song_title","song_image","audio"]



class UserRegistrationForm(UserCreationForm):

    class Meta:

        model = User 
        fields = ['username','password1','password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter username...'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter password...'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Confirm password...'})

