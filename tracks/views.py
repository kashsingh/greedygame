from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from tracks.forms import TrackForm
from tracks.models import Track
from django.db.models import Q


def listview_tracks(request):
    tracks_list = Track.objects.order_by("rating")
    query = request.GET.get("search")

    if query:
        tracks_list = tracks_list.filter(
                Q(title__icontains=query)|
                Q(genres__name__icontains=query)
        ).distinct()
    context_dict={'all_tracks':tracks_list}

    return render(request, 'tracks/tracks.html', context_dict)


def track_detail(request, track_id):
    track = get_object_or_404(Track, id=track_id)
    context_dict = {'track':track}
    context_dict['star']= range(track.rating)
    context_dict['empty_star']=range(10-track.rating)
    return render(request, 'tracks/track_detail.html', context_dict)


def add_track(request):

    form = TrackForm(request.POST or None)
    url = '/tracks'
    if form.is_valid():
        form.save(commit = True)
        return HttpResponseRedirect(url)#instance.get_absolute_url())

    context_dict = {'form': form}
    return render(request, 'tracks/add_track.html', context_dict)


def edit_track(request, track_id = None):

    track_instance = get_object_or_404(Track, id=track_id)

    form = TrackForm(request.POST or None, instance=track_instance)
    #url = '/tracks'
    # Have we been provided with a valid form?
    if form.is_valid():
        form.save(commit=True)
        return redirect(track_instance.get_absolute_url())
    context_dict= {'track_instance':track_instance,'form': form}
    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'tracks/add_track.html', context_dict)


