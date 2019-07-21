from django import forms
from .models import Image

class PictureForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
