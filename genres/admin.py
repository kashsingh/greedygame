from django.contrib import admin
from genres.models import Genre
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'views')
    search_fields = ('name',)

admin.site.register(Genre,GenreAdmin)
