from django import forms
from django.forms import ModelForm
from tournaments.models import Tournaments

class TournamentForm(ModelForm):
    class Meta:
        model=Tournaments
        fields=['name','category']
