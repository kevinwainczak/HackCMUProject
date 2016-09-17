from __future__ import unicode_literals

from django.db import models

# Person model created with all fields necessary
class Person(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    age = models.IntegerField()
    race = models.CharField(max_length=255)
    sexuality = models.CharField(max_length=255)
    roast = models.CharField(max_length=255)
    desiredTopic = models.CharField(max_length=255)
    ## the type of location is going to have to change
    ## once we find out what format jeff will need it in
    distance = models.CharField(max_length=255)
    location = models.IntegerField()
