from __future__ import unicode_literals

from django.db import models

# Create your models here.
#@python_2_unicode_compatible
class Person(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    age = models.IntegerField()
    race = models.CharField(max_length=255)
    sexuality = models.CharField(max_length=8)
    roast = models.CharField(max_length=255)
    desiredTopic = models.CharField(max_length=255)
    ## the type of location is going to have to change
    ## once we find out what format jeff will need it in
    distance = models.CharField(max_length=255)
    location = models.IntegerField()


# #@python_2_unicode_compatible
# class People(models.Model):
#     host = models.OneToOneField(Person, related_name='host')
#     person1 = models.OneToOneField(Person, related_name='person1')
#     person2 = models.OneToOneField(Person, related_name='person2')
#
# #@python_2_unicode_compatible
# class OpenConversations(models.Model):
#     conversationTopic = models.CharField(max_length=200)
#     people = models.OneToOneField(People)
#     maxPeople = 3
#     peoplePresent = models.IntegerField()
