from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def min_length_validator(value):
    if len(value) < 2:
        raise ValidationError('The username must be a minimum of 2 chars')


def year_validator(value):
    if value < 1980 or value > 2049:
        raise ValidationError('Year must be between 1980 and 2049')


class Profile(models.Model):
    MAX_LENGTH_USERNAME = 10
    MIN_AGE = 18
    MAX_PASSWORD_CHARACTERS = 30
    MAX_NAME_LENGTH = 30

    username = models.CharField(

        max_length=MAX_LENGTH_USERNAME,
        null=False,
        blank=False,
        validators=(min_length_validator,)
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=(validators.MinValueValidator(MIN_AGE),),
        blank=False,
        null=False,
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_CHARACTERS,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


class Car(models.Model):
    MAX_TYPE_CHARACTERS = 10
    SPORTS_CAR = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'

    TYPES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )
    MAX_MODEL_LENGTH = 20
    MIN_MODEL_LENGTH = 2
    MIN_PRICE = 1

    type = models.CharField(
        max_length=MAX_TYPE_CHARACTERS,
        choices=TYPES,
        blank=False,
        null=False,
    )

    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        validators=(validators.MinLengthValidator(MIN_MODEL_LENGTH),),
        blank=False,
        null=False
    )

    year = models.IntegerField(
        validators=(year_validator,),
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        validators=(validators.MinValueValidator(MIN_PRICE),),
        blank=False,
        null=False,
    )

