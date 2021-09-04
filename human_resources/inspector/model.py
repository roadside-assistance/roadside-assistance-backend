import random

from human_resources.employee.model import EmployeeModel
from django.db import models

from problem_solving.city.city import City


class InspectorModel(EmployeeModel):
    class AuthorityType(models.TextChoices):
        COUNTRY = 'COUNTRY'
        PROVINCE = 'PROVINCE'
        STATE = 'STATE'

    town_under_control = models.CharField(max_length=30, choices=City.choices, default=None)
    authority_type = models.CharField(max_length=20, choices=AuthorityType.choices, default=AuthorityType.STATE)

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
