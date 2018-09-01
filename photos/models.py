# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


def upload(self, filename):
    return "images/{}/{}/".format(self.uploaded_by, filename)


class Photo(models.Model):
    image = models.ImageField(upload_to=upload)
    location = models.CharField(blank=True, max_length=255)
    likes = models.ManyToManyField('photographers.Photographer',
                                   related_name="likes",)
    uploaded_by = models.ForeignKey('photographers.Photographer',
                                    related_name="uploaded_by")

    def __unicode__(self):
        return self.filename

    @property
    def filename(self):
        """
        Returns a filename of the image uploaded
        :rtype: str
        """
        return self.image.name
