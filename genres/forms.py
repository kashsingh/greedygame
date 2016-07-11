from django import forms

from genres.models import Genre
from django.template.defaultfilters import slugify

class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the genre name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Genre
        fields = ('name',)

    def clean(self):
        cleaned_data = super(GenreForm, self).clean()
        slug = slugify(cleaned_data['name'])
        try:
            Genre.objects.get(slug=slug)
            raise forms.ValidationError('Genre already exists.')
        except Genre.DoesNotExist:
            pass

        # Always return cleaned_data
        return cleaned_data