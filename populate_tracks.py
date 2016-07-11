import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greedymusic2.settings')

import django

django.setup()

from genres.models import Genre
from tracks.models import Track


def populate():

    """p= Genre.objects.all()
    for genre in p:
        print genre.name,genre.id"""

    with open('trackList','r') as fi:
        for title in fi:
            add_track(title)
            print "Track Added:"+title


def add_track(title=None):
    p = Track.objects.get_or_create(title=title, rating=random.randint(0,10))[0]
    id1 = random.randint(1,107)
    print id1
    gObject1 = Genre.objects.get(pk=id1)

    id2 = random.randint(1,107)
    print id2
    gObject2 = Genre.objects.get(pk=id2)
    print gObject1
    if gObject1 == gObject2:
        p.genres.add(gObject1)
    else:
        p.genres.add(gObject1, gObject2)

    p.save()
    return p



# Start execution here!
if __name__ == '__main__':
    print "Starting Greedy Music population script..."
    populate()
