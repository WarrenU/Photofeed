from rest_framework import viewsets

from .models import Photographer
from .serializers import PhotographerSerializer


class PhotographersViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Photographers to be viewed or edited.
    """
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer
