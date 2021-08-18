from django.db import models


class SkillModel(models.Model):
    name = models.CharField(max_length=255)
