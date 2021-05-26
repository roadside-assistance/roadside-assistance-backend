#!/bin/bash

# check and created new migration files if needed
docker-compose run web python manage.py makemigraions

# apply migrations to database
docker-compose run web python manage.py makemigraions
