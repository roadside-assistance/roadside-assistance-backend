from django.db import models

from human_resources.user.model import UserModel
from problem_solving.city.city import City


class CitizenModel(UserModel):
    city = models.CharField(max_length=30, choices=City.choices, default=None)
