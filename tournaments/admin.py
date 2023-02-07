from django.contrib import admin

from tournaments.models import Tournaments

# admin.site.register(Products)

@admin.register(Tournaments)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
