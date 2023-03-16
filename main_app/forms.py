from django import forms
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Photo, Post


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Mandatory.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Mandatory.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def get_absolute_url(self):
        return reverse('home', kwargs={'user_id': self.id})

class PictureForm(ModelForm):
    class Meta:
        model = Post
        fields = ['user','caption', 'date']
