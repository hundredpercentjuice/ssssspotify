from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("album", api.albumViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("album_tracker/album/", views.albumListView.as_view(), name="album_tracker_album_list"),
    path("album_tracker/album/create/", views.albumCreateView.as_view(), name="album_tracker_album_create"),
    path("album_tracker/album/detail/<int:pk>/", views.albumDetailView.as_view(), name="album_tracker_album_detail"),
    path("album_tracker/album/update/<int:pk>/", views.albumUpdateView.as_view(), name="album_tracker_album_update"),
    path("album_tracker/album/delete/<int:pk>/", views.albumDeleteView.as_view(), name="album_tracker_album_delete"),

)
