from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Commodity(models.Model):

    name = models.CharField(max_length=16)

    class Meta:

        abstract = True


class ResoldCommodity(Commodity):

    url = models.TextField()


class NormalCommodity(Commodity):

    price = models.IntegerField()


class Order(models.Model):

    commodity_type = models.ForeignKey(ContentType)
    commodity_id = models.PositiveIntegerField()
    commodity = GenericForeignKey('commodity_type', 'commodity_id')
