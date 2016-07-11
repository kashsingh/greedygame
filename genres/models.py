from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True, null='False')
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
            # Uncomment if you don't want the slug to change every time the name changes
            #if self.id is None:
                    #self.slug = slugify(self.name)
            self.slug = slugify(self.name)
            super(Genre, self).save(*args, **kwargs)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.name

    class Meta:
        verbose_name_plural = "Genres"
