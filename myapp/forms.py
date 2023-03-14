from django.forms import ModelForm
from django import forms
from .models import File, Notes

class FileForm(forms.ModelForm):
    class Meta:
        model= File
        fields= ["name", "filepath"]
# for creating file input  

class SearchForm(forms.ModelForm):
    class Meta:
        model= File
        fields= ["name"]
        
class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)


class textForm(ModelForm):
    class Meta:
        model= Notes
        fields=[
            "title",
            "text_area",
            "author",
        ]       
