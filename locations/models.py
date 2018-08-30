# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Location(models.Model):
    address = models.CharField(blank=True, max_length=255)
    coordinates = models.CharField(blank=True, max_length=255)

    def __unicode__(self):
        return '{} - {}'.format(self.address, self.coordinates)
