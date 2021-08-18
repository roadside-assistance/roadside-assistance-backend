from django.db import models

from human_resources.citizen.model import CitizenModel
from human_resources.inspector.model import InspectorModel
from human_resources.team.model import TeamModel
from problem_solving.skill.model import SkillModel


class ProblemModel(models.Model):
    class ProblemStatus(models.TextChoices):
        NEW = 'NEW'
        ASSIGNED = 'ASSIGNED'
        APPROVED = 'APPROVED'
        REJECTED = 'REJECTED'
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
    assigned_to_team = models.ForeignKey(TeamModel, on_delete=models.CASCADE, blank=True, null=True)
    assigned_to_inspector = models.ForeignKey(InspectorModel, on_delete=models.CASCADE, blank=True, null=True)
