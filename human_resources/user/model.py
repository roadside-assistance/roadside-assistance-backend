from django.db import models


class UserModel(models.Model):
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=127)
