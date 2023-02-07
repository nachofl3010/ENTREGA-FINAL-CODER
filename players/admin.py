from django.contrib import admin

from players.models import Players, Matches, Results

# admin.site.register(Products)

@admin.register(Players)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ('country',)
    search_fields = ('name',)


@admin.register(Matches)
class PlayerAdmin(admin.ModelAdmin):
    list_display=('player_1','player_2','winner','year')
    search_fields=('player_1','player_2',)

@admin.register(Results)
class ResultAdmin(admin.ModelAdmin):
    list_display=('name','tournament','result','points_earned')

