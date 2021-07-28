from human_resources.user.model import User
from django.db import models


class Employee(User):
    salary = models.BigIntegerField()
