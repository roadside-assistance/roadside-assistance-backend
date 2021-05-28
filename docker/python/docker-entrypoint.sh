#!/bin/bash

# Collect static files
#echo "Collect static files"
#python manage.py collectstatic --noinput

echo "make database migrations"
python manage.py makemigrations

echo "Apply database migrations"
python manage.py migrate

echo "starting http server"
python manage.py runserver 0.0.0.0:8000 &


echo "starting cli worker"
celery -A app worker -l INFO