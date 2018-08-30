from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Photographer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'password',
                  'email',)


class PhotographerSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = Photographer
        fields = ('id',
                  'feed',
                  'followees',
                  'followers',
                  'location',
                  'user',
                  'url')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        user = UserSerializer.create(UserSerializer(),
                                     validated_data=user_data)
        user.set_password(password)
        user.save()
        photographer = Photographer.objects.create(
            user=user,
            location=validated_data.get('location'))
        return photographer
