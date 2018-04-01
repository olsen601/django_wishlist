from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited')

class ReviewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('visited_date', 'note')
