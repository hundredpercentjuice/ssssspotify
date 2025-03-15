import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_album_list_view(client):
    instance1 = test_helpers.create_album_tracker_album()
    instance2 = test_helpers.create_album_tracker_album()
    url = reverse("album_tracker_album_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_album_create_view(client):
    url = reverse("album_tracker_album_create")
    data = {
        "artist": "text",
        "title": "text",
        "spotify_uuid": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_album_detail_view(client):
    instance = test_helpers.create_album_tracker_album()
    url = reverse("album_tracker_album_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_album_update_view(client):
    instance = test_helpers.create_album_tracker_album()
    url = reverse("album_tracker_album_update", args=[instance.pk, ])
    data = {
        "artist": "text",
        "title": "text",
        "spotify_uuid": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
