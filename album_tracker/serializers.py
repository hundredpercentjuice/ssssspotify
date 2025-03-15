from rest_framework import serializers

from . import models


class albumSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.album
        fields = [
            "artist",
            "title",
            "spotify_uuid",
            "last_updated",
            "created",
        ]
