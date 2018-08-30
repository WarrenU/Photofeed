# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from photos.models import Photo


class Photographer(models.Model):
    """
    Photographers are the users of the system.
    """
    feed = models.ManyToManyField(Photo, blank=True)
    followees = models.ManyToManyField("self", blank=True)
    followers = models.ManyToManyField("self", blank=True)
    location = models.CharField(blank=True, max_length=255)
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username
