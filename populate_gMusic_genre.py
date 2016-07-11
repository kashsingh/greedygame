import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greedymusic2.settings')

import django

django.setup()

from genres.models import Genre


def populate():

    with open('genreList','r') as fi:
        for name in fi:
            add_cat(name)
            print "Genre Added:"+name


def add_cat(name):
    c = Genre.objects.get_or_create(name=name)[0]
    c.save()
    return c


# Start execution here!
if __name__ == '__main__':
    print "Starting Greedy Music population script..."
    populate()
