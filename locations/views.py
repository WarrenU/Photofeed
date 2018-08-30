from rest_framework import viewsets

from .models import Location
from .serializers import LocationSerializer


class LocationsViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Locations to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
