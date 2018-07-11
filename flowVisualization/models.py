from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DataRecord(models.Model):
    description = models.CharField(max_length = 100, default = '')
    date = models.DateTimeField(auto_now = True)
    timeLasted = models.FloatField()
    
    maxUploadValue = models.FloatField()
    minUploadValue = models.FloatField()
    avgUploadValue = models.FloatField()
    totalUploadValue = models.FloatField()
    
    maxDownloadValue = models.FloatField()
    minDownloadValue = models.FloatField()
    avgDownloadValue = models.FloatField()
    totalDownloadValue = models.FloatField()

class TempRecord(models.Model):
    maxd = models.FloatField()
    mind = models.FloatField()
    totald = models.FloatField()

    maxu = models.FloatField()
    minu = models.FloatField()
    totalu = models.FloatField()
    
    time = models.FloatField()