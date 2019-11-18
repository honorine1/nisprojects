from django import forms
from .models import Profile,Post,Neighborhood,Business
from django.contrib.auth.forms import AuthenticationForm



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','profile']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['user','occupantsCount','image']