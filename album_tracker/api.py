from rest_framework import viewsets, permissions

from . import serializers
from . import models


class albumViewSet(viewsets.ModelViewSet):
    """ViewSet for the album class"""

    queryset = models.album.objects.all()
    serializer_class = serializers.albumSerializer
    permission_classes = [permissions.IsAuthenticated]
