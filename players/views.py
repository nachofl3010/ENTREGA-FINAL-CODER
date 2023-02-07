
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from players.models import Players, Matches, Results
from players.forms import PlayerForm, ResultForm, MatchForm
from django.views.generic import DeleteView


@login_required
def add_player(request):
    if request.method == 'GET':
        context = {
            'form': PlayerForm()
        }

        return render(request, 'players/add_player.html', context=context)

    elif request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            Players.objects.create(
                name=form.cleaned_data['name'],
                country=form.cleaned_data['country'],
                is_active=form.cleaned_data['is_active'],
            )
            context = {
                'message': 'Player added successfully'
            }
            return render(request, 'players/add_player.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': PlayerForm()
            }
            return render(request, 'players/add_player.html', context=context)

def list_players(request):
    if 'search' in request.GET:
        search = request.GET['search']
        players = Players.objects.filter(name__icontains=search)
    else:
        players = Players.objects.all()
    context = {
        'players':players,
    }
    return render(request, 'players/list_players.html', context=context)


@login_required
def update_player(request, pk):
    player = Players.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': PlayerForm(
                initial={
                    'name':player.name,
                    'country':player.country,
                    'is_active':player.is_active,

                }
            )
        }

        return render(request, 'players/update_player.html', context=context)

    elif request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player.name = form.cleaned_data['name']
            player.country = form.cleaned_data['country']
            player.is_active = form.cleaned_data['is_active']
            player.save()
            
            context = {
                'message': 'Player info updated'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': PlayerForm()
            }
        return render(request, 'players/update_player.html', context=context)



def add_match(request):
    if request.method == 'GET':
        context = {
            'form': MatchForm()
        }

        return render(request, 'matches/add_match.html', context=context)

    elif request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            Matches.objects.create(
                player_1=form.cleaned_data['player_1'],
                player_2=form.cleaned_data['player_2'],
                year=form.cleaned_data['year'],
                winner=form.cleaned_data['winner']
            )
            context = {
                'message': 'Match added successfully'
            }
            return render(request, 'matches/add_match.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': MatchForm()
            }
            return render(request, 'players/add_player.html', context=context)


def list_matches(request):
    all_matches=Matches.objects.all()
    context={
        'matches':all_matches
    }
    return render(request, 'matches/list_matches.html', context=context)

def add_result(request):
    if request.method == 'GET':
        context = {
            'form': ResultForm()
        }

        return render(request, 'results/add_result.html', context=context)

    elif request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            Results.objects.create(
                name=form.cleaned_data['name'],
                tournament=form.cleaned_data['tournament'],
                result=form.cleaned_data['result'],
                points_earned=form.cleaned_data['points_earned']
            )
            context = {
                'message': 'Result added successfully'
            }
            return render(request, 'results/add_result.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': ResultForm()
            }
            return render(request, 'results/add_result.html', context=context)

def list_results(request):
    all_results=Results.objects.all()
    context={
        'results':all_results
    }
    return render(request, 'results/list_results.html', context=context)

class PlayersDeleteView(DeleteView):
    model = Players
    template_name = 'players/delete_player.html'
    success_url = '/players/list-players/'

def about_us(request):
    return render(request, 'players/about_us.html',context={})

def federer_bio(request):
    return render(request, 'players/federer_bio.html',context={})

def nadal_bio(request):
    return render(request, 'players/nadal_bio.html',context={})

def djokovic_bio(request):
    return render(request, 'players/djokovic_bio.html',context={})

def fernandezlilli_bio(request):
    return render(request, 'players/fernandezlilli_bio.html',context={})


