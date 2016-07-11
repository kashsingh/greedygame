from django.conf.urls import url

from genres import views

urlpatterns = [url(r'^$', views.listview_genre, name='tracks'),
               url(r'^add_genre/$', views.add_genre, name='add_genre'),
               url(r'^(?P<genre_name_slug>[\w\-]+)/$', views.tracklist, name='tracklist'),
               url(r'^(?P<genre_name_slug>[\w\-]+)/edit_genre$', views.edit_genre, name='edit_genre'),
               url(r'^(?P<genre_name_slug>[\w\-]+)/(?P<track_id>[\w\-]+)/$', views.genre_track_detail, name='genre_track_detail'),
               ]