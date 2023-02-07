from django.urls import path

from tournaments.views import add_tournament, list_tournaments


urlpatterns = [
    path('add-tournament/', add_tournament),
    path('list-tournaments/', list_tournaments),
]