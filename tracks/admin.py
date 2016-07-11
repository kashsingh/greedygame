from django.contrib import admin

from tracks.models import Track


class TracksAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating')
    list_filter = ('rating',)
    search_fields = ('title',)

# Register your models here.
admin.site.register(Track,TracksAdmin)