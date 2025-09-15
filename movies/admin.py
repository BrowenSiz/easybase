from django.contrib import admin
from .models import Genre, Movie, Director, Watchlist

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_year', 'rating', 'is_published', 'director')
    list_filter = ('is_published', 'genres', 'release_year')
    search_fields = ('title',)

    readonly_fields = ('time_create', 'time_update')

    fieldsets = (
        ('Основная ифнормация', {
            'fields': ('title', 'description', 'poster')
        }),
        ('Данные о релизе', {
            'fields': (('release_year', 'rating'),)
        }),
        ('Связи', {
            'fields': ('director', 'genres')
        }),
        ('Статус', {
            'classes': ('collapse',),
            'fields': ('is_published', 'time_create', 'time_update')
        }),
    )

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    pass

@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'movie', 'watched_on')
    list_filter = ('user', 'movie')