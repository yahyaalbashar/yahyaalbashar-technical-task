from django import forms
from .models import Digimon


class UpdateDigimonForm(forms.ModelForm):
    class Meta:
        model=Digimon
        fields=['name','level','image']

    