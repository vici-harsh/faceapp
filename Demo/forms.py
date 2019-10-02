from .models import images
from django import forms
from django.forms import ModelForm

class imageForm(ModelForm):
    class Meta:
        model = images
        fields = ['Title','content_image','style_image']
        widgets = {
            'Title': forms.TextInput(attrs={ 'class' : 'form-control', 'id' : 'exampleInputEmail1', 'placeholder' : 'Enter title'})
        }
