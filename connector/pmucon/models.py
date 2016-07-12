from __future__ import unicode_literals

from django.db import models

class PendingEvent(models.Model):
  app_uid = models.CharField(max_length=200)
  status = models.CharField(max_length=200)