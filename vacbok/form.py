from django.forms import ModelForm
from .models import VacCenter
from django import forms
from django.contrib.auth.models import User
class CenterForm(ModelForm):
    class Meta:
        model = VacCenter
        fields='__all__'

class UserForm(ModelForm):
    class Meta:
        model=User
        fields= ['username','email','first_name']

class ImageUploadForm(forms.Form):
    image = forms.ImageField()



