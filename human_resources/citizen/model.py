from django.db import models
from problem_solving.city.city import City


class Citizen(models.Model):
    city = models.CharField(max_length=30, choices=City.choices, default=None)
