from django import forms

class WorksForm(forms.Form):
    file      = forms.FileField() # for creating file input  
    