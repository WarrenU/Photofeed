from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from comments.models import Comment
from comments.serializers import CommentSerializer
from .models import Photo
from .serializers import PhotoSerializer


class PhotosViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Photos to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    @action(detail=True)
    def comments(self, request, pk):
        """
        Endpoint for querying Comments on a photo.
        """
        photo = Photo.objects.get(id=pk)
        comments = Comment.objects.filter(photo=photo)
        serializer = CommentSerializer(comments,
                                       many=True,
                                       context={'request': request})
        return Response(serializer.data)
