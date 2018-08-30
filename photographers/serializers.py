from rest_framework import serializers

from .models import Photographer


class PhotographerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photographer
        fields = ('feed',
                  'followees',
                  'followers',
                  'location',
                  'user',)
