from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abbreviation = models.CharField(max_length=2, null=True)

    def __unicode__(self):
        return self.name


class StateCapital(models.Model):
    name = models.CharField(max_length=100)
    state = models.OneToOneField("main.State", null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    population = models.IntegerField(null=True)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    state = models.ForeignKey("main.State")
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def __unicode__(self):
        return self.name
