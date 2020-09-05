from django import forms
from .models import FinnModel


#create a Form
class FinnForm(forms.ModelForm):

    #creating Meta Class
    class Meta:
        model:FinnModel
        fields=['title', 'description',]





