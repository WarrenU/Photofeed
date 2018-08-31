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

    def list(self, request, *args, **kwargs):
        """
        Returns serialized data of Photo objects, that are within the same
        location as the user (Photographer).
        """
        photographer = request.user.photographer
        photo_feed = (Photo
                      .objects
                      .filter(location__icontains=photographer.location))
        for photo in photo_feed:
            photographer.feed.add(photo)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
