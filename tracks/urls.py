from django.conf.urls import url

from tracks import views

urlpatterns = [url(r'^$', views.listview_tracks, name='tracks'),
               url(r'^add_track/$', views.add_track, name='add_track'),
               url(r'^(?P<track_id>[\w\-]+)/$', views.track_detail, name='track_detail'),
               url(r'^(?P<track_id>[\w\-]+)/edit_track/$', views.edit_track, name='track_edit'),

                ]