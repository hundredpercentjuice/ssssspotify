from django import forms
from . import models


class albumForm(forms.ModelForm):
    class Meta:
        model = models.album
        fields = [
            "artist",
            "title",
            "spotify_uuid",
        ]
