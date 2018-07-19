# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Images(models.Model):
    img_url = models.CharField(max_length=100)
