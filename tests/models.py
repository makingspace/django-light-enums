from django.db import models

from django_light_enums import enum


class Status(enum.Enum):
    STATUS_ONE = 1
    STATUS_TWO = 2
    STATUS_THREE = 5923


class DbModel(models.Model):

    status = enum.EnumField(Status)
