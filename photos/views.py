from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from photographers.models import Photographer
from .models import Photo
from .serializers import PhotoSerializer


class PhotosViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Photographers to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    @action(detail=True)
    def feed(self, request, pk):
        """
        Get photo feed of a Photographer (user), that is within the
        photographers location and excluding all photos they uploaded.
        """
        photographer = Photographer.objects.get(id=pk)
        uploaded_photos = (
            Photo
            .objects
            .filter(location=photographer.location)
            .exclude(uploaded_by=photographer)
        )
        serializer = self.get_serializer(uploaded_photos, many=True)
        return Response(serializer.data)
