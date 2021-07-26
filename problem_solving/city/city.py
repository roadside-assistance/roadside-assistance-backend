from django.db import models


class City(models.TextChoices):
    TEHRAN = 'TEHRAN'
    MASHAHD = 'MASHHAD'
    SHIRAZ = 'SHIRAZ'
    ESFAHAN = 'ESFAHAN'
    TABRIZ = 'TABRIZ'
    KASHAN = 'KASHAN'
