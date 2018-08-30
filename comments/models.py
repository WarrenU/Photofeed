# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from photographers.models import Photographer
from photos.models import Photo


class Comment(models.Model):
    comment = models.TextField()
    commented_by = models.ForeignKey(Photographer)
    photo = models.ForeignKey(Photo)

    def __unicode__(self):
        return self.comment
