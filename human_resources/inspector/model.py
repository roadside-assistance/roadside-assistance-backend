from human_resources.employee.model import Employee
from django.db import models

from problem_solving.city.city import City


class Inspector(Employee):
    town_under_control = models.CharField(max_length=30, choices=City.choices, default=None)
