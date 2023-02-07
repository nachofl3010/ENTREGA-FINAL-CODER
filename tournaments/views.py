from django.shortcuts import render

from django.http import HttpResponse
from tournaments.models import Tournaments
from tournaments.forms import TournamentForm
from django.contrib.auth.decorators import login_required

@login_required
def add_tournament(request):
    if request.method == 'GET':
        context = {
            'form': TournamentForm()
        }

        return render(request, 'tournaments/add_tournament.html', context=context)

    elif request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            Tournaments.objects.create(
                name=form.cleaned_data['name'],
                category=form.cleaned_data['category']
            )
            context = {
                'message': 'Tournament added successfully'
            }
            return render(request, 'tournaments/add_tournament.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': TournamentForm()
            }
            return render(request, 'tournaments/add_tournament.html', context=context)

def list_tournaments(request):
    all_tournaments=Tournaments.objects.all()
    context={
        'tournaments':all_tournaments
    }
    return render(request, 'tournaments/list_tournaments.html', context=context)


