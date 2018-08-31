from rest_framework import viewsets
from rest_framework.response import Response

from photos.models import Photo
from photos.serializers import PhotoSerializer
from .models import Photographer
from .serializers import PhotographerSerializer


class PhotographersViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Photographers to be viewed or edited.
    """
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer
