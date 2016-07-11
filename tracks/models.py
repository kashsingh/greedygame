from __future__ import unicode_literals

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from genres.models import Genre
# Create your models here.

class Track(models.Model):

    title = models.CharField(max_length=128)
    genres = models.ManyToManyField(Genre)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        print "ran method"+str(self.id)
        return reverse('tracks.views.track_detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Tracks"