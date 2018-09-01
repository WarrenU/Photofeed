from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
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
        serializer = PhotoSerializer(photo_feed,
                                     many=True,
                                     context={'request': request})
        return Response(serializer.data)

    @action(methods=['post'], detail=True,
            permission_classes=[IsAuthenticated])
    def follow(self, request, pk):
        logged_in_photographer = get_object_or_404(Photographer,
                                                   user=request.user)
        photographer_to_follow = get_object_or_404(Photographer, id=pk)
        logged_in_photographer.follow_handshake(photographer_to_follow)
        return Response({'status': status.HTTP_200_OK})

