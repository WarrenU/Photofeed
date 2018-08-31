from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from photographers.models import Photographer
from .models import Photo
from .serializers import PhotoSerializer


class PhotosViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Photos to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    @action(detail=True)
    def feed(self, request, pk):
        """
        Get photo feed for photographer, giving them a queryset of Photos
        near their location, and uploaded by photographers they are following.
        """
        photographer = Photographer.objects.get(id=pk)
        photo_feed = (
            Photo
            .objects
            .filter(Q(location__istartswith=photographer.location) |
                    Q(uploaded_by__in=photographer.following.all()))
            .exclude(uploaded_by=photographer)
        )
        serializer = self.get_serializer(photo_feed, many=True)
        return Response(serializer.data)
