import random

from human_resources.employee.model import EmployeeModel
from django.db import models

from problem_solving.city.city import City


class InspectorModel(EmployeeModel):
    town_under_control = models.CharField(max_length=30, choices=City.choices, default=None)

    @classmethod
    def random(cls):
        ids = cls.objects.values('id')
        if len(ids) > 0:
            random_id = random.choice(ids)["id"]

            try:
                inspector = cls.objects.get(pk=random_id)
            except cls.DoesNotExist:
                inspector = None

            return inspector
