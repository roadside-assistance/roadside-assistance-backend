from django.db import models


class TeamModel(models.Model):
    name = models.CharField(max_length=255)
