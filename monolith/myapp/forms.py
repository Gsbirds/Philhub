from django.forms import ModelForm
from django import forms
from .models import File, Notes
from django.forms import Textarea
# from django.contrib.auth.forms import UserChangeForm, UserCreationForm 
# from .models import CustomUser 

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
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)


class textForm(ModelForm):
    class Meta:
        model= Notes
        fields=[
            "title",
            "text_area",
        ]       
        widgets = {
            'title': Textarea(attrs={
                'class': "form-control1",
                'style': 'max-width: 300px;',
                'placeholder': 'Title'
                }),
            'text_area': Textarea(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': ''
                })
        }


# class CustomUserCreationForm(UserCreationForm):    
#     class Meta:        
#         model = CustomUser        
#         fields = ('email', )  
# class CustomUserChangeForm(UserChangeForm):    
#     class Meta:        
#         model = CustomUser        
#         fields = UserChangeForm.Meta.fields