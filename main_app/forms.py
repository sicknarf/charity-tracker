from django.forms import ModelForm
from django import forms
from .models import Donation, DONOS

class NewDonoForm(ModelForm):
    class Meta:
        model = Donation
        fields = ['amount', 'donator', 'pokemon' ]
        amount = forms.CharField(
            label='choose the amount donated',
            widget=forms.Select(choices=DONOS),)