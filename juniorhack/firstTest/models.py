from __future__ import unicode_literals

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Person(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    age = models.IntegerField()
    race = models.CharField(max_length=255)
    sexuality = models.CharField(max_length=8)
    roast = models.CharField(max_length=255)
    ## the type of location is going to have to change
    ## once we find out what format jeff will need it in
    location = models.CharField(max_length=255)


@python_2_unicode_compatible
class People(models.Model):
    person1 = models.ForeignKey(Person)
    person2 = models.ForeignKey(Person)
    person3 = models.ForeignKey(Person)
    person4 = models.ForeignKey(Person)

@python_2_unicode_compatible
class OpenConversations(models.Model):
    conversationTopic = models.CharField(max_length=200)
    people = models.ForeignKey(People)
