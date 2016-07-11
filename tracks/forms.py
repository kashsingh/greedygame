from django import forms

from genres.models import Genre
from tracks.models import Track

class TrackForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the track title.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all())
    rating = forms.ChoiceField(choices=[(x, x) for x in range(0, 11)])

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Track
        exclude = ('views', )

