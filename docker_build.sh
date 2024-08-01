#!/bin/bash

set -e

if [ $# -eq 1 ]; then
  sudo docker login --username andrewjw --password $DOCKER_TOKEN
fi

sudo docker buildx create --use

sudo docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 \
                         --build-arg VERSION=$TAG \
                         -t andrewjw/foxessprom:$TAG \
                         -t andrewjw/foxessprom:latest \
                         $1 .
