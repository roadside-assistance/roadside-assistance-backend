from django.db import models

from humanResources.models.citizen import Citizen
# from problemSolving.tasks import notify_expert


class ProblemModel(models.Model):
    # TYPE_CHOICES = [
    #     ('first', 'First type'),
    #     ('second', 'Second type'),
    #     ('third', 'Third type'),
    # ]

    STATUS_CHOICES = [
        ('waiting_to_be_assigned', 'Waiting to be assigned'),
        ('waiting_to_be_checked', 'Waiting to be checked'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    issuer = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    description = models.TextField()
    # type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    address = models.TextField()
    type = models.TextField()
    status = models.CharField(max_length=22, choices=STATUS_CHOICES, default='waiting_to_be_assigned')
    needed_devices = models.CharField(max_length=1000,blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)
        # notify_expert(self.id)
