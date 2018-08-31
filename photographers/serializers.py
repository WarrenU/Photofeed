from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers

from photographers.helpers import get_updated_obj
from .models import Photographer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'password',
                  'email',)
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
        }


class PhotographerSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = Photographer
        fields = ('id',
                  'followers',
                  'following',
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

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        photographer_data = validated_data
        user = get_updated_obj(user_data, instance.user)
        user.set_password(password)
        user.save()
        photographer = get_updated_obj(photographer_data, instance)
        photographer.save()
        return photographer
