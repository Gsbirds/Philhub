from django import forms
from .models import File

class FileForm(forms.ModelForm):
    class Meta:
        model= File
        fields= ["name", "filepath"]
# for creating file input  
    