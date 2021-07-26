from django.db import models

from human_resources.citizen.model import Citizen


class ProblemModel(models.Model):
    class ProblemStatus(models.TextChoices):
        NEW = 'NEW'
        ASSIGNED = 'ASSIGNED'
        APPROVED = 'APPROVED'
        REJECTED = 'REJECTED'

    issuer = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    address = models.TextField()
    description = models.TextField()
    status = models.CharField(max_length=20, choices=ProblemStatus.choices, default=ProblemStatus.NEW)
