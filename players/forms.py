from django import forms
from players.models import Players, Results
from tournaments.models import Tournaments
from django.forms import ModelForm

class PlayerForm(forms.Form):
    name = forms.CharField(max_length=100)
    is_active = forms.BooleanField(required=False)
    country= forms.CharField(max_length=100)

class ResultForm(ModelForm):
    #tournament = forms.ModelChoiceField(Tournaments.objects.values_list())
    class Meta:
        model=Results
        fields=['name','result','points_earned','tournament']



class MatchForm(forms.Form):
    player_1=forms.CharField(max_length=100)
    player_2=forms.CharField(max_length=100)
    year=forms.FloatField()
    winner=forms.CharField(max_length=100)