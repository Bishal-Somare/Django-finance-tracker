from django import forms
#tala ko chai user creation ko lagi ho hai ta usercreationform import garna parcha
from django.contrib.auth.forms import UserCreationForm
#tala ko chai user ko model ho hai ani tyo database ma rakna ko lagi ho hai
from django.contrib.auth.models import User
from . models import Transcation


class RegisterForm(UserCreationForm):
    #yedi kunai field yeha chaina bhana maila 
    # email= forms.EmailField() yo use garna paauchu
    class Meta:
        model= User
        fields=['username','email','password1','password2']

class TranscationForm(forms.ModelForm):
    class Meta:
        model=Transcation
        fields=['title','amount','date','transcation_type','category']

