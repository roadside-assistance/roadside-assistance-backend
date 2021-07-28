from django.db import models

from human_resources.user.model import User
from problem_solving.city.city import City


class Citizen(User):
    city = models.CharField(max_length=30, choices=City.choices, default=None)
