from django.db import models

from human_resources.employee.model import Employee
from human_resources.team.model import Team


class Worker(Employee):
    team = models.ForeignKey(Team)
