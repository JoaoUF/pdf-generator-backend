from django.db import models
from utils.model import Model
from django_extensions.db.models import ActivatorModel, TimeStampedModel


class Profile(ActivatorModel, TimeStampedModel, Model):
    name = models.CharField(
        db_column='name',
        max_length=200
    )
    email = models.EmailField(
        db_column='email',
    )
    phone = models.CharField(
        db_column='phone',
        max_length=200
    )
    summary = models.CharField(
        db_column='summary',
        max_length=200
    )
    degree = models.CharField(
        db_column='degree',
        max_length=200
    )
    school = models.CharField(
        db_column='school',
        max_length=200
    )
    university = models.CharField(
        db_column='university',
        max_length=200
    )
    previousWork = models.TextField(
        db_column='previous_work',
        max_length=1000
    )
    skills = models.TextField(
        db_column='skills',
        max_length=1000
    )

    def __str__(self):
        self.name

    class Meta:
        db_table = 'MAE_PROFILE'
