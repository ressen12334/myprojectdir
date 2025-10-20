from colorsys import yiq_to_rgb

from django.db import models
from django import forms

from django.db.models import F, Value, CharField

class District(models.Model):
    dcode = models.CharField(null=True, blank=True,max_length=4)
    lcode = models.CharField(null=True, blank=True,max_length=3)
    name = models.CharField(null=True, blank=True,max_length=40)
    office = models.CharField(null=True, blank=True,max_length=200)
    contact = models.CharField(null=True, blank=True,max_length=200)
    phone = models.CharField(null=True, blank=True,max_length=100)
    region = models.CharField(null=True, blank=True,max_length=40)
    r = models.CharField(null=True, blank=True, max_length=3)
    def __str__(self):
        return f"{self.lcode}{"_"}{self.name}{" "}{self.r}"

class Suguan(models.Model):
    week = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date = models.DateTimeField("Date-Time")
    day = models.CharField(max_length=100)
    locale = models.CharField(max_length=100)

