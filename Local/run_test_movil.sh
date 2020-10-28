#!/bin/bash
current_dir=$(dirname $(realpath "$0"))

# JOB_NAME is the name of the project of this build. This is the name you gave your job. It is set up by Jenkins
COMPOSE_ID=${JOB_NAME:-local}

# Remove Previous Stack, only for Jenkins
# docker-compose -f $current_dir/docker-compose.yml -f $current_dir/compose-grid.yml --env-file=$current_dir/.env -p $COMPOSE_ID rm -f

# Starting new stack environment
docker-compose -f $current_dir/docker-compose.yml -f $current_dir/compose-grid.yml --env-file=$current_dir/.env -p $COMPOSE_ID up --build --force-recreate --remove-orphans