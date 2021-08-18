from django.db import models

from human_resources.citizen.model import CitizenModel
from problem_solving.skill.model import SkillModel


class MachineModel(models.Model):
    class MachineStatus(models.TextChoices):
        RESERVED = 'RESERVED'
        RELEASED = 'RELEASED'

    class MachineType(models.TextChoices):
        TYPE1 = 'ONE'
        TYPE2 = 'TWO'
        TYPE3 = 'THREE'

    name = models.CharField(max_length=127)
    type = models.CharField(max_length=20, choices=MachineType.choices, default=None)
    status = models.CharField(max_length=20, choices=MachineStatus.choices, default=MachineStatus.RELEASED)
