# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


def upload(self):
    return "images/{}/".format(self.photographer)


class Photo(models.Model):
    image = models.ImageField(upload_to=upload)
    location = models.CharField(blank=True, max_length=255)
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
