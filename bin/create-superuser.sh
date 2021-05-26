#!/bin/bash

# create django admin superuser
docker-compose run web python manage.py createsuperuser
