from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    id_doc = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=50, null=False, blank=False)


class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(null=False, blank=False)


class Sport(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)


class Team(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
