# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Movie(models.Model):
    """This class create the data representation of the app"""
    name = models.CharField(max_length=100)
    year_of_release = models.PositiveSmallIntegerField()

    def __str__(self):
        """This method converts name object to a human readable string"""