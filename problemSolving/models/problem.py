from django.db import models

from humanResources.models.citizen import Citizen


class Problem(models.Model):
    TYPE_CHOICES = [
        ('first', 'First type'),
        ('second', 'Second type'),
        ('third', 'Third type'),
    ]

    STATUS_CHOICES = [
        ('waiting_for_check', 'Waiting for Check'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    issuer = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    description = models.TextField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    status = models.CharField(max_len=20, choices=STATUS_CHOICES)
