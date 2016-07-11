from genres.models import Genre
from tracks.models import Track
from genres.forms import GenreForm
from django.shortcuts import redirect
from tracks.views import track_detail
from django.shortcuts import render, get_object_or_404
from django.db.models import Q


def listview_genre(request):
    genre_list = Genre.objects.order_by("name")
    query = request.GET.get("search")

    if query:
        genre_list = genre_list.filter(
                Q(name__icontains=query)
        ).distinct()

    context_dict= {'all_genres': genre_list}

    return render(request, 'genres/genres.html', context_dict)


def add_genre(request):
    # A HTTP POST?

    if request.method == 'POST':
        form = GenreForm(request.POST)
        url = '/genres'
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            return redirect(url)
            # Now call the index() view.
            # The user will be shown the homepage.
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = GenreForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'genres/add_genre.html', {'form': form})


def tracklist(request, genre_name_slug):
    context_dict={}

    try:
        genre = Genre.objects.get(slug=genre_name_slug)

        context_dict['genre_name']= genre.name

        all_tracks= Track.objects.filter(genres=genre)

        context_dict['track_list']=all_tracks
        context_dict['genre']=genre

    except Genre.DoesNotExist:
        pass

    return render(request, 'genres/track_list.html', context_dict)

def genre_track_detail(request, genre_name_slug, track_id):

    return track_detail(request,track_id)


def edit_genre(request, genre_name_slug=None):
    genre_instance = get_object_or_404(Genre, slug=genre_name_slug)
    url="/genres"
    form = GenreForm(request.POST or None, instance=genre_instance)
    # Have we been provided with a valid form?
    if form.is_valid():
        form.save(commit=True)
        return redirect(url)
    context_dict= {'genre_instance':genre_instance,'form': form}
    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'genres/add_genre.html', context_dict)


