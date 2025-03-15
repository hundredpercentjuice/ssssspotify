from django.contrib import admin
from django import forms

from . import models


class albumAdminForm(forms.ModelForm):

    class Meta:
        model = models.album
        fields = "__all__"


class albumAdmin(admin.ModelAdmin):
    form = albumAdminForm
    list_display = [
        "artist",
        "title",
        "spotify_uuid",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "artist",
        "title",
        "spotify_uuid",
        "last_updated",
        "created",
    ]


admin.site.register(models.album, albumAdmin)
