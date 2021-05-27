#!/bin/bash

# exit if any sub-command fails
set -e

echo "Setting appropriate file permission."
sudo chown -R $USER: ../

# Prevent git to commit permission changes.
git config --global core.fileMode false

rm -f ../.env
touch ../.env

echo POSTGRES_DB=postgres >> .env
echo POSTGRES_USER=postgres >> .env
echo POSTGRES_PASSWORD=postgres >> .env
echo POSTGRES_PORT=5432 >> .env
echo DJANGO_PORT=8000 >> .env
echo POSTGRES_DATA_DIR=./storage/postgres >> .env


echo -n "Please set Shecan.ir DNS (to this file /etc/resolv.conf on ubuntu) to start pulling docker images, then press ENTER to continue..."
read notice

docker-compose pull
docker-compose build
docker-compose up -d
