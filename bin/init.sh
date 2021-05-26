#!/bin/bash

# exit if any sub-command fails
set -e

echo "Setting appropriate file permission."
sudo chown -R $USER: ../

# Prevent git to commit permission changes.
git config --global core.fileMode false

#rm -f ../.env
#touch ../.env

#echo POSTGRES_DB=0.0.0.0 >> .env

echo -n "Please set Shecan.ir DNS (to this file /etc/resolv.conf on ubuntu) to start pulling docker images, then press ENTER to continue..."
read notice

docker-compose pull
docker-compose build
docker-compose up -d
