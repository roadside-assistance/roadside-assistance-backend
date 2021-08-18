from django.db import models

from human_resources.employee.model import EmployeeModel
from human_resources.team.model import TeamModel


class WorkerModel(EmployeeModel):
    team = models.ForeignKey(TeamModel, on_delete=models.CASCADE)
