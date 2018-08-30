# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from locations.models import Location


def upload(self):
    return "images/{}/".format(self.photographer)


class Photo(models.Model):
    file = models.ImageField(upload_to=upload)
    location = models.ForeignKey(Location)
    likes = models.ManyToManyField('photographers.Photographer',
                                   related_name="likes")
    uploaded_by = models.ForeignKey('photographers.Photographer',
                                    related_name="uploaded_by")

    def __unicode__(self):
        return self.filename

    @property
    def filename(self):
        """
        Returns a filename of the image uploaded `file`
        :rtype: str
        """
        return self.file.name
