import random

from django.db import models
from django.db.models.signals import post_save

from human_resources.citizen.model import CitizenModel
from human_resources.inspector.model import InspectorModel
from human_resources.team.model import TeamModel
from machine_resources.machine.model import MachineModel
from problem_solving.skill.model import SkillModel


class ProblemModel(models.Model):
    class ProblemStatus(models.TextChoices):
        NEW = 'NEW'
        ASSIGNED = 'ASSIGNED'
        APPROVED = 'APPROVED'
        REJECTED = 'REJECTED'
        PENDING_TEAM = 'PENDING_TEAM'
        STARTED = 'STARTED'
        ENDED = 'ENDED'

    class ProblemNeededSkills(models.TextChoices):
        SKILL1 = 'ONE'
        SKILL2 = 'TWO'
        SKILL3 = 'THREE'

    issuer = models.ForeignKey(CitizenModel, on_delete=models.CASCADE)
    address = models.TextField()
    description = models.TextField()
    status = models.CharField(max_length=20, choices=ProblemStatus.choices, default=ProblemStatus.NEW)
    number_of_needed_workers = models.IntegerField(default=None)
    needed_skills = models.ManyToManyField(SkillModel)
    needed_machines = models.ManyToManyField(MachineModel)
    assigned_to_team = models.ForeignKey(TeamModel, on_delete=models.CASCADE, blank=True, null=True)
    assigned_to_inspector = models.ForeignKey(InspectorModel, on_delete=models.CASCADE, blank=True, null=True)


def assign_to_inspector(sender, instance: ProblemModel, **kwargs):
    if instance.status == ProblemModel.ProblemStatus.NEW:
        inspector = InspectorModel.random()
        instance.assigned_to_inspector = inspector
        instance.status = ProblemModel.ProblemStatus.ASSIGNED
        instance.save()
    elif instance.status == ProblemModel.ProblemStatus.APPROVED:
        team = TeamModel.random()
        instance.assigned_to_team = team
        instance.status = ProblemModel.ProblemStatus.PENDING_TEAM
        instance.save()


post_save.connect(assign_to_inspector, sender=ProblemModel)
