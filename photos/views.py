from rest_framework import viewsets

from .models import Photo
from .serializers import PhotoSerializer


class PhotosViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Photographers to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
