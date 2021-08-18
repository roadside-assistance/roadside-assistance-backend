from human_resources.employee.model import EmployeeModel
from django.db import models

from problem_solving.city.city import City


class InspectorModel(EmployeeModel):
    town_under_control = models.CharField(max_length=30, choices=City.choices, default=None)
