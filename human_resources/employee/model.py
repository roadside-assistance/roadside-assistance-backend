from human_resources.user.model import UserModel
from django.db import models


class EmployeeModel(UserModel):
    salary = models.BigIntegerField()
