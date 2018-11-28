from django.db import models
from django.conf import settings

# Create your models here.

from django.db import models
from django.utils import timezone

class HistImage(models.Model):
    Photograph = models.ImageField(null=True, blank=True, upload_to="static")
    Photographer_FirstName = models.CharField(max_length=50, null=True, blank=True)
    Photographer_MiddleName = models.CharField(max_length=50, null=True, blank=True)
    Photographer_LastName = models.CharField(max_length=50, null=True, blank=True)
    Title = models.CharField(max_length=200, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    DescriptionLong = models.TextField(null=True, blank=True)
    Province = models.CharField(max_length=50, null=True, blank=True)
    County = models.CharField(max_length=50, null=True, blank=True)
    City =  models.CharField(max_length=50, null=True, blank=True)
    Year = models.IntegerField(null=True, blank=True)
    Season = models.CharField(max_length=20, null=True, blank=True)
    CoordinatesN = models.FloatField(null=True, blank=True)
    CoordinatesE = models.FloatField(null=True, blank=True)
    DateTaken = models.DateTimeField(blank=True, null=True)
    Contributor_FirstName = models.CharField(max_length=50, null=True, blank=True)
    Contributor_LastName = models.CharField(max_length=50, null=True, blank=True)
    Contributor_Email = models.EmailField(null=True, blank=True)
    Contributor_Organization = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.Title






