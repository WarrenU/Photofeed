# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Comments to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
