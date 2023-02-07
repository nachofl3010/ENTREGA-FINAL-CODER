from django.urls import path

from players.views import add_player, list_players, add_match, list_matches, add_result, list_results,PlayersDeleteView,update_player,about_us,federer_bio,djokovic_bio,fernandezlilli_bio,nadal_bio

urlpatterns = [
    path('add-player/', add_player),
    path('list-players/', list_players),
    path('add-match/', add_match),
    path('list-matches/', list_matches),
    path('add-result/', add_result),
    path('list-results/', list_results),
    path('delete-player/<int:pk>/', PlayersDeleteView.as_view(), name='delete_player'),
    path('update-player/<int:pk>/',update_player, name='update_player'),
    path('about-us/',about_us,name='about_us'),
    path('federer-bio/',federer_bio),
    path('djokovic-bio/',djokovic_bio),
    path('nadal-bio/',nadal_bio),
    path('player-bio/6/',fernandezlilli_bio),
    path('player-bio/1/',federer_bio),
    path('player-bio/4/',djokovic_bio),
    path('player-bio/3/',nadal_bio),


]