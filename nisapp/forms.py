from django import forms
from .models import Profile,Post,Neighborhood,Business
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['admin']

    

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['admin'  ]
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class UserUpdate(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1']
