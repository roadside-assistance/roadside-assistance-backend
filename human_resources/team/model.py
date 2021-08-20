import random

from django.db import models

from human_resources.worker.model import WorkerModel


class TeamModel(models.Model):
    name = models.CharField(max_length=255)
    leader = models.ForeignKey(WorkerModel, on_delete=models.CASCADE, related_name='leader')
    members = models.ManyToManyField(WorkerModel, related_name='member')

    @classmethod
    def random(cls):
        ids = cls.objects.values('id')
        if len(ids) > 0:
            random_id = random.choice(ids)["id"]

            try:
                inspector = cls.objects.get(pk=random_id)
            except cls.DoesNotExist:
                inspector = None

            return inspector

