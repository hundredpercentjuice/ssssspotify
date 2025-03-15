from django.db import models
from django.urls import reverse


class album(models.Model):

    # Fields
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    spotify_uuid = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("album_tracker_album_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("album_tracker_album_update", args=(self.pk,))

